from typing import List, Type

from blue_assistant.script.repository.generic import GenericScript
from blue_assistant.script.repository.blue_amo.classes import BlueAmoScript
from blue_assistant.script.repository.mining_on_moon.classes import MiningOnMoonScript

list_of_script_classes: List[Type[GenericScript]] = [
    GenericScript,
    BlueAmoScript,
    MiningOnMoonScript,
]

list_of_script_names: List[str] = [
    script_class.name for script_class in list_of_script_classes
]
