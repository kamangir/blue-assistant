from blueness import module

from blue_assistant import NAME
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


def set_light_color(
    color: str,
    light: str,
    verbose: bool = False,
) -> bool:
    logger.info(f"{NAME}.set_light_color: {color} -> {light}")

    logger.info("🪄")

    return True
