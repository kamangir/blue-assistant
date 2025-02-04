from blueness import module
from blue_objects import objects
from openai_commands.image_generation.api import OpenAIImageGenerator

from blue_assistant import NAME
from blue_assistant.env import (
    BLUE_ASSISTANT_IMAGE_DEFAULT_MODEL,
    BLUE_ASSISTANT_IMAGE_DEFAULT_SIZE,
    BLUE_ASSISTANT_IMAGE_DEFAULT_QUALITY,
)
from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


# https://platform.openai.com/docs/guides/images
def generate_image(
    script: BaseScript,
    node_name: str,
) -> bool:
    logger.info(f"{NAME}: {script} @ {node_name} ...")

    generator = OpenAIImageGenerator(
        model=BLUE_ASSISTANT_IMAGE_DEFAULT_MODEL,
        verbose=script.verbose,
    )

    filename = f"{node_name}.png"

    success = generator.generate(
        prompt=script.nodes[node_name]["prompt"],
        filename=objects.path_of(
            filename=filename,
            object_name=script.object_name,
            create=True,
        ),
        quality=(BLUE_ASSISTANT_IMAGE_DEFAULT_QUALITY if script.test_mode else "hd"),
        size=(BLUE_ASSISTANT_IMAGE_DEFAULT_SIZE if script.test_mode else "1792x1024"),
        sign_with_prompt=False,
    )[0]

    if success:
        script.nodes[node_name]["filename"] = filename

    return success
