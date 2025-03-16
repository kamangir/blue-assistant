import pytest

from blue_assistant.web.functions import normalize_url


@pytest.mark.parametrize(
    ["url", "expected_output"],
    [
        [
            "https://ode.rsl.wustl.edu/account/login.aspx?ReturnUrl=index.aspx#section",
            "https://ode.rsl.wustl.edu/account/login.aspx",
        ],
        [
            "https://example.com/view?ReturnUrl=home&session=123#details",
            "https://example.com/view",
        ],
        [
            "https://example.com/search?query=python&session=xyz#results",
            "https://example.com/search",
        ],
    ],
)
def test_web_normalize_url(
    url: str,
    expected_output: str,
):
    assert normalize_url(url) == expected_output
