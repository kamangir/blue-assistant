import os

from blue_objects import file, README

from blue_assistant import NAME, VERSION, ICON, REPO_NAME


items = [
    "[`{}`]({}) [![image]({})]({}) {}".format(
        item["title"],
        item["url"],
        item["marquee"],
        item["url"],
        item["description"],
    )
    for item in [
        {
            "title": "orbital-data-explorer",
            "url": "./blue_assistant/script/repository/orbital_data_explorer/README.md",
            "marquee": "https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true",
            "description": "Access to the [Orbital Data Explorer](https://ode.rsl.wustl.edu/), through AI.",
        },
        {
            "title": "blue-amo",
            "url": "./blue_assistant/script/repository/blue_amo/README.md",
            "marquee": "https://github.com/kamangir/assets/raw/main/blue-amo-2025-02-03-nswnx6/stitching_the_frames-2.png?raw=true",
            "description": "A story developed and visualized, by AI.",
        },
    ]
]


def build():
    return all(
        README.build(
            items=readme.get("items", []),
            path=os.path.join(file.path(__file__), readme["path"]),
            ICON=ICON,
            NAME=NAME,
            VERSION=VERSION,
            REPO_NAME=REPO_NAME,
        )
        for readme in [
            {"items": items, "path": ".."},
            {"path": "script/repository/blue_amo"},
            {"path": "script/repository/orbital_data_explorer"},
        ]
    )
