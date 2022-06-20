from datetime import datetime
from pathlib import Path

import frontmatter
import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

from ssg.backlinks import inject_internal_links
from ssg.models import Page, Site


def inject_title(page: Page):
    page['title'] = page['metadata'].get('title')


def inject_date(page: Page, site: Site):
    date = page['metadata'].get('date')
    if date is None:
        return None
    date_format = page['metadata'].get('date_format', site['date_format'])
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


def compile_markdown(page: Page, site: Site):
    inject_raw_markdown(page)
    inject_title(page)
    inject_date(page, site)
    inject_date_iso8601(page)
    inject_full_name(page)
    inject_html(page)
    inject_internal_links(page)
    inject_layout(page)
