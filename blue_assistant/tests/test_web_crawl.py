from typing import List
import pytest

from blue_objects import objects

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
    seed_urls: List[str],
):
    object_name = objects.unique_object("test_web_crawl")

    success, crawl_cache = crawl_list_of_urls(
        seed_urls=seed_urls,
        object_name=object_name,
        max_iterations=max_iterations,
    )

    assert success
    assert isinstance(crawl_cache, dict)
    assert len(crawl_cache)
