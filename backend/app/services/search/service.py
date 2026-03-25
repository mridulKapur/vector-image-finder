from app.infrastructure.models.base import EmbeddingModel
from app.infrastructure.vector_store.base import VectorStore

class SearchService:
    def __init__(self, embedder, vector_store):
        self.embedder:EmbeddingModel = embedder
        self.vector_store:VectorStore = vector_store
        return

    def search(self, query: str):
        """
        Search for images based on the provided query string.
        """
        queryEmbedding = self.embedder.embed_text(query)
        results = self.vector_store.search_vector(queryEmbedding,limit=10)
        print("results",results)
        return results
