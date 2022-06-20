import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List

import frontmatter
import markdown
import sass
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown.extensions.wikilinks import WikiLinkExtension
from tqdm import tqdm
from typing_extensions import TypedDict

from backlinks import inject_backlinks, inject_internal_links

DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S %z'

jinja_env = Environment(
    loader=FileSystemLoader("theme/layouts"),
    autoescape=select_autoescape()
)


class Site(TypedDict, total=False):
    title: str
    url: str
    pages: List['Page']


class Page(TypedDict, total=False):
    url: str  # local path on the site to the page
    path: Path  # absolute path to the markdown
    target_path: Path  # absolute path where to
    metadata: Dict  # frontmatter data
    content: str  # markdown text
    html: str  # raw html
    layout: str  # 'default.html'


def inject_title(page: Page):
    page['title'] = page['metadata'].get('title')


def inject_date(page: Page):
    date = page['metadata'].get('date')
    if date is None:
        return None
    date_format = page['metadata'].get('date_format', DEFAULT_DATE_FORMAT)
    page['date'] = datetime.strptime(date, date_format)


def inject_date_iso8601(page: Page):
    # 2013-05-16T08:36:00+00:00
    if page.get('date') is not None:
        page['date_iso8601'] = page['date'].isoformat()


def inject_full_name(page: Page):
    page['full_name'] = page['path'].with_suffix('').name


def new_page(
    src: Path,
    root_dir_path: Path,
    dest_dir_path: Path,
) -> Page:
    rel_path = src.relative_to(root_dir_path)
    target_path = dest_dir_path / rel_path
    url = '/' + str(rel_path.with_suffix(''))
    target_path = target_path.with_suffix('.html')
    return Page(
        url=url,
        path=src,
        target_path=target_path,
    )


def inject_raw_markdown(page):
    text = page['path'].read_text()
    metadata, content = frontmatter.parse(text)
    page['metadata'] = metadata
    page['content'] = content


def inject_html(page):
    extensions = [
        'markdown.extensions.tables',
        WikiLinkExtension(base_url='/', end_url=''),
        'pymdownx.arithmatex',
        'pymdownx.highlight',
        'pymdownx.magiclink',
        'pymdownx.superfences',
    ]
    page['html'] = markdown.markdown(
        page['content'],
        extensions=extensions,
    )


def inject_layout(page: Page):
    layout = page['metadata'].get('layout', 'default')
    if not layout.endswith('.html'):
        layout += '.html'
    page['layout'] = layout


def process(page: Page):
    inject_raw_markdown(page)
    inject_title(page)
    inject_date(page)
    inject_date_iso8601(page)
    inject_full_name(page)
    inject_html(page)
    inject_internal_links(page)
    inject_layout(page)


def render_page(page: Page, site: Site):
    template = jinja_env.get_template(page['layout'])
    full_html = template.render(
        site=site,
        page=page,
    )
    page['target_path'].parent.mkdir(exist_ok=True, parents=True)
    page['target_path'].write_text(full_html)


def compile_content(src: Path, dst: Path):
    site = Site(
        title="Senior Sigan's garden",
        url='/',
    )
    site['pages'] = [
        new_page(entry, src, dst)
        for entry in sorted(src.rglob('*.md'))
    ]
    for page in tqdm(site['pages']):
        process(page)

    inject_backlinks(site)

    for page in tqdm(site['pages']):
        render_page(page, site)


def compile_sass(
    src: Path,
    dst: Path,
):
    css = sass.compile(
        filename=str(src.absolute()),
        output_style='compressed',
        include_paths=str(src.parent.absolute()),
    )

    dst.parent.mkdir(exist_ok=True)
    dst.write_text(css)


def copy_assets(src: Path, dst: Path):
    shutil.copytree(src, dst, dirs_exist_ok=True)


def main():
    compile_content(Path('content'), Path('build'))
    compile_sass(Path('theme/styles/app.scss'), Path('build/app.css'))
    copy_assets(Path('content/assets'), Path('build/assets'))


if __name__ == '__main__':
    main()
