from blueness import module

from blue_assistant import NAME
from blue_assistant.logger import logger


NAME = module.name(__file__, NAME)


def chat(
    object_name: str,
    interactive: bool = True,
) -> bool:
    logger.info(
        "{}.chat -{}> {}".format(
            NAME,
            object_name,
            "interactive-" if interactive else "",
        )
    )

    return True
