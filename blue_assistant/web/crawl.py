from typing import List, Dict, Set, Tuple
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse

from blueness import module
from blue_options.logger import log_long_text, log_list

from blue_assistant import NAME
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


def fetch_links_and_content(
    url: str,
    verbose: bool = False,
) -> Tuple[Set, str]:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        return set(), ""

    soup = BeautifulSoup(response.text, "html.parser")
    links = set()

    for a_tag in soup.find_all("a", href=True):
        a_url = urljoin(url, a_tag["href"])

        if a_url.startswith(url):
            logger.info(f"+= {a_url}")
            links.add(a_url)
            continue

        logger.info(f"ignored: {a_url}")

    plain_text = soup.get_text(separator=" ", strip=True)

    if verbose:
        log_list(logger, list(links), "link(s)")
        log_long_text(logger, plain_text)

    return links, plain_text


def crawl_list_of_urls(
    seed_urls: List[str],
    object_name: str,
    max_iterations: int = 10,
    verbose: bool = False,
) -> Dict[str, str]:
    logger.info(
        "{}.crawl_list_of_urls({}): {} -> {}".format(
            NAME,
            len(seed_urls),
            ", ".join(seed_urls),
            object_name,
        )
    )

    visited: Dict[str, str] = {}
    queue: Set[str] = set(seed_urls)

    iteration: int = 0
    while queue:
        current_url = queue.pop()
        if current_url in visited:
            continue

        logger.info(f"🔗  {current_url} ...")
        new_links, content = fetch_links_and_content(
            url=current_url,
            verbose=verbose,
        )
        visited[current_url] = content
        queue.update(new_links - visited.keys())

        iteration += 1
        if max_iterations != -1 and iteration >= max_iterations:
            logger.warning(f"max iteration of {max_iterations} reached.")
            break

    if queue:
        logger.warning(f"queue: {len(queue)}")

    return visited
