from blueness import module

from blue_assistant import NAME
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


def set_light_color(
    bridge_ip: str,
    username: str,
    light_id: str,
    hue: int,  # 0 to 65535
    saturation: int,  # 0 to 254
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.set_light_color({}@{}:{}) -> hue=0x{:x}, saturation=0x{:x}".format(
            NAME,
            username,
            bridge_ip,
            light_id,
            hue,
            saturation,
        )
    )

    ...

    return True
