from typing import List, Dict, Tuple, Type

from blue_assistant.script.actions.generic import GenericAction
from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.script.actions import list_of_actions

from blue_assistant.logger import logger


def get_action_class(
    action_name: str,
) -> Tuple[bool, Type[GenericAction]]:
    for action_class in list_of_actions:
        if action_class.name == action_name:
            return True, action_class

    logger.error(f"{action_name}: action not found.")
    return False, GenericAction


def perform_action(
    action_name: str,
    script: BaseScript,
    node_name: str,
) -> Tuple[bool, Dict]:
    success, action_class = get_action_class(action_name=action_name)
    if not success:
        return False, {
            "error": f"{action_name}: action not found.",
        }

    action_object = action_class(
        script=script,
    )

    return action_object.perform(
        node_name=node_name,
    )
