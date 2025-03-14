from typing import List

from blue_options.terminal import show_usage, xtra


def help_set(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    args = [
        "[--light <light>",
        "[--color <color>]",
    ]

    return show_usage(
        [
            "@hue",
            "set",
            f"[{options}]",
        ]
        + args,
        "blue-plugin node <object-name>.",
        mono=mono,
    )


help_functions = {
    "set": help_set,
}
