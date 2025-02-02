from typing import List

from blue_options.terminal import show_usage, xtra
from abcli.help.generic import help_functions as generic_help_functions

from blue_assistant import ALIAS
from blue_assistant.help.script import help_functions as help_script


def help_browse(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "actions|repo"

    return show_usage(
        [
            "@assistant",
            "browse",
            f"[{options}]",
        ],
        "browse blue_assistant.",
        mono=mono,
    )


help_functions = generic_help_functions(plugin_name=ALIAS)

help_functions.update(
    {
        "browse": help_browse,
        "script": help_script,
    }
)
