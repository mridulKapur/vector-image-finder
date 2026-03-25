import uuid
from app.infrastructure.vector_store.base import VectorStore
from app.infrastructure.models.base import EmbeddingModel
from app.infrastructure.blob_store.base import StorageBackend

class IndexingService:
    def __init__(self, embedder:EmbeddingModel, vector_store:VectorStore, storage:StorageBackend):
        self.embedder = embedder
        self.vector_store = vector_store
        self.storage = storage

    def index_image(self, image_id: str):
        image_path = self.storage.get_image_url(image_id)
        image = self.storage.load_image(image_path)
        image_metadata = self.storage.get_image_metadata(image_path)
        if not image:
            Exception("Image not found")
        
        embeddings = self.embedder.embed_images([image])
        embedding = embeddings[0]
        point = {"id":image_id,"vector":embedding,"payload":image_metadata}
        self.vector_store.upsert_points([point])
        return


    def index_folder(self, folder_path: str) -> int:
        images = self.storage.load_images(folder_path)
        image_metadata = self.storage.get_images_metadata(folder_path)

        if not images:
            return 0

        embeddings = self.embedder.embed_images(images)

        points = [{"id":uuid.uuid4(),"vector":vec,"payload":image_metadata} for vec,image_metadata in zip(embeddings,image_metadata)]

        self.vector_store.upsert_points(points)

        return len(images)
