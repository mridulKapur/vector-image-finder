# embedding_model/base.py
from abc import ABC, abstractmethod
from typing import List


class EmbeddingModel(ABC):

    @abstractmethod
    def embed_images(self, images) -> List[float]:
        pass

    @abstractmethod
    def embed_text(self, text: str) -> List[float]:
        pass
