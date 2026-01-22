# vector_store/implementations/qdrant_store.py
from typing import List
from qdrant_client import QdrantClient
from qdrant_client.http import models as rest
from qdrant_client.models import PointStruct

from backend.store.base import VectorStore, VectorPoint
from ...app.config import QDRANT_URL, QDRANT_COLLECTION, EMBED_DIM


class QdrantVectorStore(VectorStore):

    def __init__(self):
        self._client = QdrantClient(url=QDRANT_URL)
        self._ensure_collection()

    def _ensure_collection(self):
        try:
            print(f"Fetching collection: {QDRANT_COLLECTION}")
            self._client.get_collection(collection_name=QDRANT_COLLECTION)
        except Exception:
            print(f"Collection not found. Creating {QDRANT_COLLECTION}")
            vector_config = rest.VectorParams(
                size=EMBED_DIM,
                distance=rest.Distance.COSINE
            )
            self._client.create_collection(
                collection_name=QDRANT_COLLECTION,
                vectors_config=vector_config
            )

    def upsert_points(self, points: List[VectorPoint]) -> None:
        qdrant_points = [
            PointStruct(
                id=p["id"],
                vector=p["vector"],
                payload=p["payload"]
            )
            for p in points
        ]
        self._client.upsert(
            collection_name=QDRANT_COLLECTION,
            points=qdrant_points
        )

    def search_vector(self, vector: List[float], limit: int = 20):
        result = self._client.query_points(
            collection_name=QDRANT_COLLECTION,
            query=vector,
            limit=limit,
            with_payload=True
        )
        return result.points
