import pytest

from blue_assistant.web.fetch import fetch_links_and_text


@pytest.mark.parametrize(
    ["url"],
    [
        ["https://ode.rsl.wustl.edu/"],
    ],
)
def test_web_fetch(
    url: str,
):
    summary = fetch_links_and_text(url=url)

    for key, type_ in {
        "links": set,
        "text": str,
    }.items():
        assert key in summary
        assert isinstance(summary[key], type_)
