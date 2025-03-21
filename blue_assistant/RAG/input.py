import PyPDF2 as pypdf
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def pdf_to_faiss(
    pdf_location,
    chunk_size=800,
    chunk_overlap=100,
):
    pdf = pypdf.PdfReader(pdf_location)

    full_text = ""
    for content in pdf.pages:
        raw_text = content.extract_text()
        full_text += raw_text

    text_splits = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=800,
        chunk_overlap=100,
        length_function=len,
    ).split_text(full_text)

    embeddings = HuggingFaceEmbeddings()

    db = FAISS.from_texts(text_splits, embeddings)

    return db
