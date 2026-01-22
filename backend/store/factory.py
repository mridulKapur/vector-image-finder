from .base import VectorStore
from implementations.qdrant_store import QdrantVectorStore


_vector_store: VectorStore | None = None


def get_vector_store() -> VectorStore:
    global _vector_store
    if _vector_store is None:
        _vector_store = QdrantVectorStore()
    return _vector_store
