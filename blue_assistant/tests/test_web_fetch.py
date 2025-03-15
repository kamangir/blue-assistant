import pytest

from blue_assistant.web.functions import fetch_links_and_text


@pytest.mark.parametrize(
    ["url"],
    [
        ["https://ode.rsl.wustl.edu/"],
    ],
)
def test_web_fetch(
    url: str,
):
    links, plain_text = fetch_links_and_text(url=url)

    assert isinstance(links, set)
    assert isinstance(plain_text, str)
