from blueness import module

from blue_assistant import NAME
from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


def researching_the_questions(
    script: BaseScript,
    node_name: str,
) -> bool:
    logger.info(f"{NAME}: ...")

    logger.info("🪄")

    return True
