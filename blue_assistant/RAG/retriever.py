import faiss
from transformers import AutoTokenizer, AutoModel


class Retriever:
    def __init__(
        self,
        index_path,
        model_name="sentence-transformers/all-MiniLM-L6-v2",
    ):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.index = faiss.read_index(index_path)

    def encode(
        self,
        texts,
    ):
        inputs = self.tokenizer(
            texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
        )
        outputs = self.model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1).detach().numpy()
        return embeddings

    def retrieve(self, query, top_k=5):
        query_embedding = self.encode([query])
        distances, indices = self.index.search(query_embedding, top_k)
        return indices[0]
