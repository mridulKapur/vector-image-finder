# embedding_model/base.py
from abc import ABC, abstractmethod
from typing import List
from PIL import Image

class EmbeddingModel(ABC):

    @abstractmethod
    def embed_images(self, images:List[Image.Image]) -> List[float]:
        pass

    @abstractmethod
    def embed_text(self, text: str) -> List[float]:
        pass
