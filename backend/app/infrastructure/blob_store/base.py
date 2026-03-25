from abc import ABC, abstractmethod
from PIL import Image
from fastapi import UploadFile

class ImageData:
    def __init__(self, path: str, metadata: dict):
        self.path = path
        self.metadata = metadata

class StorageBackend(ABC):
    @abstractmethod
    async def save_images(self,images:list[UploadFile]) -> list[str]:
        pass

    @abstractmethod
    def load_image(self, source: str) -> list[Image.Image]:
        pass
    
    @abstractmethod
    def get_image_metadata(self,image_id:str) -> ImageData:
        pass

    @abstractmethod
    def get_image_url(self, image_id:str) -> str:
        pass