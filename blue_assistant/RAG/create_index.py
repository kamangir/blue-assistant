import numpy as np
import faiss
from retriever import Retriever

documents = [
    "Document 1 content...",
    "Document 2 content...",
    "Document 3 content...",
]  # Your documents
retriever = Retriever(index_path=None)  # Initialize without index

embeddings = retriever.encode(documents)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, "path_to_faiss_index")
