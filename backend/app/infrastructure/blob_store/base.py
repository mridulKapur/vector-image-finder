from abc import ABC, abstractmethod

class ImageData:
    def __init__(self, path: str, metadata: dict):
        self.path = path
        self.metadata = metadata

class StorageBackend(ABC):

    @abstractmethod
    def load_images(self, source: str) -> list[ImageData]:
        pass
    
    @abstractmethod
    def get_images_metadata(self,source:str) -> list[ImageData]:
        pass