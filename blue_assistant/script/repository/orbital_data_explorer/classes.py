from blue_objects import file, path

from blue_assistant.script.repository.generic.classes import GenericScript


class OrbitalDataExplorerScript(GenericScript):
    name = path.name(file.path(__file__))
