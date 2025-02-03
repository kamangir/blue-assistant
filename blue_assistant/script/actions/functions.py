from typing import List, Dict, Tuple, Type

from blueness import module
from blue_assistant.script.actions.generic import GenericAction
from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.script.actions import list_of_actions

from blue_assistant import NAME
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


def get_action_class(
    action_name: str,
) -> Tuple[bool, Type[GenericAction]]:
    for action_class in list_of_actions:
        if action_class.name == action_name:
            return True, action_class

    logger.error(f"{action_name}: action not found.")
    return False, GenericAction
