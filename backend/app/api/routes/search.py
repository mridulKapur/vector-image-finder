from fastapi import APIRouter
from app.api.schemas import SearchRequest, SearchResponse

router = APIRouter()

@router.post("/")
def search(request: SearchRequest):
    """
    Search images by text or image.
    """
    return SearchResponse(results=[])
