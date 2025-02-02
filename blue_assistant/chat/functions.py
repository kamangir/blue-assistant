from blueness import module
from blue_options.terminal.functions import hr

from blue_assistant import NAME, ICON
from blue_assistant.chat.context import ChatContext
from blue_assistant.logger import logger


NAME = module.name(__file__, NAME)


def chat(
    object_name: str,
    interactive: bool = True,
    verbose: bool = False,
    load_history: bool = True,
) -> bool:
    logger.info(
        "{}.chat -{}> {}".format(
            NAME,
            "interactive-" if interactive else "",
            object_name,
        )
    )

    context = ChatContext(
        object_name,
        load_history=load_history,
    )

    logger.info('Type in "help" for help.')

    while True:
        prompt = input(f"{ICON}  > ") if interactive else ""

        state = context.process(prompt)
        if state is False:
            logger.info("chat failed.")
            return False
        if state is None:
            logger.info("end of chat.")
            break

        if not interactive:
            break

        print(hr(width=21))

    return context.save()
