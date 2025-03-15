import pytest

from blue_assistant.web.functions import url_to_filename


@pytest.mark.parametrize(
    ["max_length"],
    [
        [10],
        [100],
        [1000],
    ],
)
@pytest.mark.parametrize(
    ["url"],
    [
        ["https://ode.rsl.wustl.edu/"],
        ["https://pds-geosciences.wustl.edu/dataserv/default.htm"],
        ["https://github.com/samiriff/mars-ode-data-access"],
    ],
)
def test_url_to_filename(
    url: str,
    max_length: int,
):
    filename = url_to_filename(
        url=url,
        max_length=max_length,
    )

    assert len(filename) <= max_length
