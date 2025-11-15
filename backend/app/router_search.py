from fastapi import APIRouter, Query
from typing import List
from .clip_model import embed_text
from .qdrant_client import search_vector

router = APIRouter()

@router.get("/search")
async def search(q: str = Query(..., description="Search text"), limit: int = 20):
    vec = embed_text(q)
    hits = search_vector(vec, limit=limit)
    results = []
    for h in hits:
        payload = h.payload if hasattr(h, 'payload') else h.payload
        results.append({
        "path": payload.get("path"),
        "score": getattr(h, 'score', None)
        })
    return {"results": results}