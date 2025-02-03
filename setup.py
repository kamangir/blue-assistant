from blue_assistant import NAME, VERSION, DESCRIPTION, REPO_NAME
from blueness.pypi import setup

setup(
    filename=__file__,
    repo_name=REPO_NAME,
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.help",
        f"{NAME}.script",
        f"{NAME}.script.actions",
        f"{NAME}.script.repository",
        f"{NAME}.script.repository.blue_amo",
        f"{NAME}.script.repository.generic",
        f"{NAME}.script.repository.moon_datasets",
    ],
    include_package_data=True,
    package_data={
        NAME: [
            "config.env",
            "sample.env",
            ".abcli/**/*.sh",
        ],
    },
)
