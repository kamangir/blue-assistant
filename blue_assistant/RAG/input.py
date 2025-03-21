import PyPDF2 as pypdf
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from blueness import module

from blue_assistant import NAME
from blue_assistant.logger import logger

NAME = module.name(__file__, NAME)


def pdf_to_faiss(
    pdf_location: str,
    chunk_size: int = 800,
    chunk_overlap: int = 100,
):
    pdf = pypdf.PdfReader(pdf_location)

    logger.info(
        "{}.pdf_to_faiss({}): loaded {} page(s)".format(
            NAME,
            pdf_location,
            len(pdf.pages),
        )
    )

    full_text = ""
    for content in pdf.pages:
        raw_text = content.extract_text()
        full_text += raw_text

    text_splits = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    ).split_text(full_text)

    embeddings = HuggingFaceEmbeddings()

    db = FAISS.from_texts(text_splits, embeddings)

    return db
