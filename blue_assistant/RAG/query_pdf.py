from typing import Tuple

from blueness import module
from blue_objects import file, objects
from blue_objects.metadata import post_to_object

from blue_assistant import NAME
from blue_assistant.RAG.input import pdf_to_faiss
from blue_assistant.RAG.output import answer
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


def query_pdf(
    object_name: str,
    filename: str,
    question: str,
    verbose: bool = False,
) -> Tuple[bool, str]:
    logger.info(
        '{}: "{}" on {}/{}'.format(
            NAME,
            question,
            object_name,
            filename,
        )
    )

    full_filename = objects.path_of(
        filename=filename if filename.endswith(".pdf") else f"{filename}.pdf",
        object_name=object_name,
    )

    db = pdf_to_faiss(full_filename)

    prompt, docs, ans = answer(db, question)

    logger.info(f"prompt: {prompt}")
    logger.info(f"docs: {docs}")
    logger.info(f"ans: {ans}")

    return (
        post_to_object(
            object_name,
            NAME.replace(".", "-"),
            {
                "prompt": prompt,
                "ans": ans,
            },
        ),
        ans,
    )
