from qdrant_client import QdrantClient
from qdrant_client.http import models as rest
from .config import QDRANT_URL, QDRANT_COLLECTION, EMBED_DIM


_qdrant = None

def get_qdrant():
    global _qdrant  
    if _qdrant is None:
        _qdrant = QdrantClient(url=QDRANT_URL)
    # ensure collection exists
    try:
        print(f"Trying to fetch collection : {QDRANT_COLLECTION} ...")
        _qdrant.get_collection(collection_name=QDRANT_COLLECTION)
    except Exception:
        print(f"Collection {QDRANT_COLLECTION} not found.")
        vector_config = rest.VectorParams(size=EMBED_DIM, distance=rest.Distance.COSINE)
        _qdrant.create_collection(collection_name=QDRANT_COLLECTION, vectors_config=vector_config)
    return _qdrant




def upsert_points(points: list):
    """Points: list of tuples (id, vector, payload)"""
    q = get_qdrant()
    # qdrant-client accepts points as a list of tuples (id, vector, payload)
    q.upsert(collection_name=QDRANT_COLLECTION, points=points)




def search_vector(vector: list, limit: int = 20):
    q = get_qdrant()
    hits = q.query_points(collection_name=QDRANT_COLLECTION, query=vector, limit=limit,with_payload=True).points
    # for h in hits:
    print(hits)
    return hits