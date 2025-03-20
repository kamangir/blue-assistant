from blue_assistant.RAG.generator import Generator
from blue_assistant.RAG.retriever import Retriever


class RAGSystem:
    def __init__(self, retriever, generator, documents):
        self.retriever = retriever
        self.generator = generator
        self.documents = documents

    def generate_response(self, query):
        retrieved_indices = self.retriever.retrieve(query)
        retrieved_documents = [self.documents[i] for i in retrieved_indices]
        prompt = query + "\n" + "\n".join(retrieved_documents)
        response = self.generator.generate(prompt)
        return response


# Example usage
if __name__ == "__main__":
    documents = [
        "Document 1 content...",
        "Document 2 content...",
        "Document 3 content...",
    ]  # Your documents
    retriever = Retriever(index_path="path_to_faiss_index")
    generator = Generator(model_name="gpt2")

    rag_system = RAGSystem(retriever, generator, documents)
    query = "What is retrieval-augmented generation?"
    response = rag_system.generate_response(query)
    print(response)
