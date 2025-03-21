import numpy as np
import faiss

from blue_assistant.RAG.retriever import Retriever


def main():
    documents = [
        "Document 1 content...",
        "Document 2 content...",
        "Document 3 content...",
    ]  # Your documents
    retriever = Retriever()  # Initialize without index

    print("Encoding documents...")
    embeddings = retriever.encode(documents)
    print("Embeddings shape:", embeddings.shape)

    print("Creating FAISS index...")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    print("Adding embeddings to index...")
    index.add(embeddings)

    print("Writing index to file...")
    faiss.write_index(index, "path_to_faiss_index")
    print("Index creation complete.")


if __name__ == "__main__":
    main()
