import logging
from html.parser import HTMLParser
from urllib.parse import urlparse

logger = logging.getLogger()


class InternalLinksExtractor(HTMLParser):
    def __init__(self, *, convert_charrefs: bool = ...) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.links = set()

    def handle_starttag(self, tag, attrs) -> None:
        if tag == 'a':
            for k, v in attrs:
                if k == 'href':
                    url = urlparse(v)
                    if not url.scheme and not url.netloc:
                        self.links.add(v)


def inject_internal_links(page):
    '''Finds all local links and save them as 'links'.
    Local link is the link with empty scheme and empty netloc.
    Examples: "<a href="/internal_link/">", "<a href="internal_link/">.
    '''
    parser = InternalLinksExtractor()
    parser.feed(page['html'])
    page['links'] = parser.links


def inject_backlinks(site):
    backlinks = {}
    pages_dict = {}
    for page in site['pages']:
        backlinks[page['url']] = set()
        pages_dict[page['url']] = page

    for page in site['pages']:
        for link in page['links']:
            if backlinks.get(link) is None:
                logger.warning(
                    f"Bad link {link} at {page['path']}")
            else:
                backlinks[link].add(page['url'])

    for page in site['pages']:
        links = backlinks.get(page['url'], set())
        page['backlinks'] = [pages_dict[link] for link in links]


def __test():
    page = {
        'html': '''
        <ul>
            <li><a href="/internal_link/">Internal 1</a></li>
            <li><a href="internal_link/test/">Internal 2</a></li>
            <li><a href="http://example.com">External</a></li>
            <li><a href="https://example.com">External</a></li>
            <li><a href="ftp://example.com">External</a></li>
            <li><a href="//example.com">External</a></li>
        </ul>
        '''
    }
    inject_internal_links(page)
    print(page['links'])
    assert("/internal_link/" in page['links'])
    assert("internal_link/test/" in page['links'])
    assert(len(page['links']) == 2)


if __name__ == '__main__':
    __test()
