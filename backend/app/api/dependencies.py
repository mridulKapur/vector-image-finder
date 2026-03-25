from app.services.indexing.service import IndexingService
from app.services.upload.service import UploadService
from app.services.search.service import SearchService
from fastapi import BackgroundTasks
from app.infrastructure.models.factory import get_embedding_model
from app.infrastructure.vector_store.factory import get_vector_store
from app.infrastructure.blob_store.implementations.local import LocalStorage

def get_indexing_service():
    return IndexingService(
        embedder=get_embedding_model(),
        vector_store=get_vector_store(),
        storage=LocalStorage(),
    )

def get_upload_service(background_tasks: BackgroundTasks):
    return UploadService(
        storage=LocalStorage(),
        background_task=background_tasks,
        embedder=get_embedding_model(),
        vector_store=get_vector_store(),
    )

def get_search_service():
    return SearchService(
        embedder=get_embedding_model(),
        vector_store=get_vector_store(),
    )