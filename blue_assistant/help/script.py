from typing import List

from blue_options.terminal import show_usage, xtra

from blue_assistant.script.repository import list_of_script_names


def help_run(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("download,dryrun,~upload", mono=mono)

    script_options = "script=<script>"

    args = ["--verbose 1"]

    return show_usage(
        [
            "@assistant",
            "script",
            "run",
            f"[{options}]",
            f"[{script_options}]",
            "[-|<object-name>]",
        ]
        + args,
        "run <object-name>.",
        {
            "script: {}".format(" | ".join(list_of_script_names)): [],
        },
        mono=mono,
    )


help_functions = {"run": help_run}
