import pytest

from blue_assistant.web.crawl import fetch_links_and_content


@pytest.mark.parametrize(
    ["url"],
    [
        ["https://ode.rsl.wustl.edu/"],
    ],
)
def test_web_fetch(
    url: str,
):
    links, plain_text = fetch_links_and_content(url=url)

    assert isinstance(links, set)
    assert isinstance(plain_text, str)
