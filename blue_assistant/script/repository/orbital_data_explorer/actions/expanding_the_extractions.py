from blueness import module

from blue_assistant import NAME
from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


def expanding_the_extractions(
    script: BaseScript,
    node_name: str,
) -> bool:
    logger.info(NAME)

    # import ipdb

    # ipdb.set_trace()

    logger.info("🪄")

    return True
