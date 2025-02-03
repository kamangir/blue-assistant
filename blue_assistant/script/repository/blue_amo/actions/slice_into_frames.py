from blueness import module

from blue_assistant import NAME
from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


def slice_into_frames(
    script: BaseScript,
    node_name: str,
) -> bool:
    logger.info(f"{NAME}: processing the output...")

    list_of_frame_prompts = script.nodes[node_name]["output"].split("---")
    if len(list_of_frame_prompts) != script.vars["frame_count"]:
        logger.warning(
            "{} != {}, frame count doesn't match, bad AI! 😁".format(
                len(list_of_frame_prompts),
                script.vars["frame_count"],
            )
        )

    list_of_frame_prompts += script.vars["frame_count"] * [""]

    for index in range(script.vars["frame_count"]):
        node_name = f"generating-frame-{index+1:03d}"

        script.nodes[node_name]["prompt"] = script.nodes[node_name]["prompt"].replace(
            ":::input",
            list_of_frame_prompts[index],
        )

    return True
