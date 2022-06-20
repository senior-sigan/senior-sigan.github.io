from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from typing_extensions import TypedDict


class Sass(TypedDict, total=False):
    src: str
    style: str
    dst: str


class Markdown(TypedDict, total=False):
    src: str
    dst: str


class Assets(TypedDict, total=False):
    src: str
    dst: str


class Layouts(TypedDict, total=False):
    src: str


class Site(TypedDict, total=False):
    title: str
    url: str
    date_format: str

    markdown: Markdown
    sass: Sass
    layouts: Layouts
    assets: Assets

    pages: List['Page']


def default_site() -> Site:
    return Site(
        title='Site',
        url='/',
        date_format='%Y-%m-%d %H:%M:%S %z',
        markdown=Markdown(
            src='content',
            dst='build',
        ),
        assets=Assets(
            src='content/assets',
            dst='build/assets',
        ),
        layouts=Layouts(
            src='theme/layouts',
        ),
        sass=Sass(
            src='theme/styles',
            style='compressed',
            dst='build/app.css',
        ),
    )


class Metadata(TypedDict, total=False):
    date_format: str  # default is '%Y-%m-%d %H:%M:%S %z'
    date: Optional[str]


class Page(TypedDict, total=False):
    url: str  # link to the page
    path: Path  # absolute path to the source file
    target_path: Path  # absolute path where to save the rendered page
    metadata: Dict  # frontmatter data
    content: str  # markdown text
    html: str  # raw html
    layout: str  # 'default.html'
    date: Optional[datetime]
    date_iso8601: Optional[str]  # 2006-01-02T15:04:05+07:00
