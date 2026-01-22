from abc import ABC, abstractmethod
from typing import List, Any
from .types import VectorPoint

SearchResult = Any


class VectorStore(ABC):

    # Add new points in the vector DB
    @abstractmethod
    def upsert_points(self, points: List[VectorPoint]) -> None:
        pass

    # Search for new points in the vector DB
    @abstractmethod
    def search_vector(self, vector: List[float], limit: int = 20) -> List[SearchResult]:
        pass