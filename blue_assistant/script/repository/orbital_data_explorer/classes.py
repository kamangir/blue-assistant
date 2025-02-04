from blue_objects import file, path

from blue_assistant.script.repository.generic.classes import GenericScript
from blue_assistant.script.repository.orbital_data_explorer.actions import (
    dict_of_actions,
)


class OrbitalDataExplorerScript(GenericScript):
    name = path.name(file.path(__file__))

    def perform_action(
        self,
        node_name: str,
    ) -> bool:
        if not super().perform_action(node_name=node_name):
            return False

        if node_name in dict_of_actions:
            return dict_of_actions[node_name](
                script=self,
                node_name=node_name,
            )

        return True
