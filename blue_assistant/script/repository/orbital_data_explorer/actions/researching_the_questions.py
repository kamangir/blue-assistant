from blueness import module

from blue_assistant import NAME
from blue_assistant.web.crawl import crawl_list_of_urls
from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


def researching_the_questions(
    script: BaseScript,
    node_name: str,
) -> bool:
    logger.info(f"{NAME}: ...")

    visited_urls = crawl_list_of_urls(
        seed_urls=script.vars["seed_urls"],
        object_name=script.object_name,
        max_iterations=script.nodes[node_name]["max_iterations"],
    )

    logger.info("🪄")

    script.nodes[node_name]["visited_urls"] = visited_urls

    return True
