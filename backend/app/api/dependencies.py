from app.domain.indexing.service import IndexingService

from app.infrastructure.models.factory import get_embedding_model
from app.infrastructure.vector_store.factory import get_vector_store
from app.infrastructure.blob_store.implementations.local import LocalStorage

def get_indexing_service():
    return IndexingService(
        embedder=get_embedding_model(),
        vector_store=get_vector_store(),
        storage=LocalStorage(),
    )
