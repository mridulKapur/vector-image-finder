import uuid
from app.services.indexing.service import IndexingService
from fastapi import UploadFile,BackgroundTasks
from app.infrastructure.blob_store.base import StorageBackend
from app.infrastructure.models.base import EmbeddingModel
from app.infrastructure.vector_store.base import VectorStore

class UploadService:
    def __init__(self, storage: StorageBackend,background_task:BackgroundTasks,embedder:EmbeddingModel,vector_store:VectorStore):
        self.storage = storage
        self.background_task = background_task
        self.embedder = embedder
        self.vector_store = vector_store

    async def upload(self,file:UploadFile):
        """
        Generates a unique image ID and a placeholder upload URL.
        """
        # In a real-world scenario with S3, this would generate a pre-signed URL.
        ids = await self.storage.save_images([file])
        self.background_task.add_task(IndexingService(embedder=self.embedder,vector_store=self.vector_store,storage=self.storage).index_image,ids[0])
        return {
            "image_id": ids[0],
            "upload_url": self.storage.get_image_url(ids[0])
        }

