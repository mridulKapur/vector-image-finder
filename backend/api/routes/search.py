from fastapi import APIRouter, Query

from ...models.factory import get_embedding_model
from ...store.factory import get_vector_store

router = APIRouter()
embedding_model = get_embedding_model()
vector_store = get_vector_store()

@router.get("/search")
async def search(q: str = Query(..., description="Search text"), limit: int = 20):
    vec = embedding_model.embed_text(q)
    hits = vector_store.search_vector(vec, limit=limit)
    results = []
    for h in hits:
        payload = h.payload if hasattr(h, 'payload') else h.payload
        results.append({
        "path": payload.get("path"),
        "score": getattr(h, 'score', None)
        })
    return {"results": results}