from typing import List

from blue_options.terminal import show_usage, xtra


def help_set(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    args = [
        "[--bridge_ip <bridge_ip>]",
        "[--username <username>]",
        "[--light_id <light_id>]",
        "[--hue <65535>]",
        "[--saturation <254>]",
        "[--verbose 1]",
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
