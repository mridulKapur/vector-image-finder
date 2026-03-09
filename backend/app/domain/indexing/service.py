import uuid
from app.infrastructure.vector_store.base import VectorStore
from app.infrastructure.models.base import EmbeddingModel
from app.infrastructure.blob_store.base import StorageBackend

class IndexingService:
    def __init__(self, embedder, vector_store, storage):
        self.embedder:EmbeddingModel = embedder
        self.vector_store:VectorStore = vector_store
        self.storage:StorageBackend = storage

    def index_folder(self, folder_path: str) -> int:
        images = self.storage.load_images(folder_path)
        image_metadata = self.storage.get_images_metadata(folder_path)

        if not images:
            return 0

        embeddings = self.embedder.embed_images(images)

        points = [{"id":uuid.uuid4(),"vector":vec,"payload":image_metadata} for vec,image_metadata in zip(embeddings,image_metadata)]

        self.vector_store.upsert_points(points)

        return len(images)
