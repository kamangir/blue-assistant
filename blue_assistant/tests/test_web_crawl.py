import pytest
from blue_assistant.web.crawl import crawl_list_of_urls


@pytest.mark.parametrize(
    ["max_iterations", "seed_urls"],
    [
        [
            2,
            [
                "https://ode.rsl.wustl.edu/",
                "https://oderest.rsl.wustl.edu/",
                "https://pds-geosciences.wustl.edu/dataserv/default.htm",
                "https://github.com/samiriff/mars-ode-data-access",
            ],
        ],
    ],
)
def test_web_crawl(
    max_iterations: int,
):
    output = crawl_list_of_urls(
        max_iterations=max_iterations,
    )

    assert isinstance(output, dict)
    assert len(output)
