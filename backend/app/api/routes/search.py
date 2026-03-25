from fastapi import APIRouter
from app.api.schemas import SearchRequest, SearchResponse
from app.services.search.service import SearchService
from app.api.dependencies import get_search_service
from fastapi import Depends

router = APIRouter()

@router.post("/")
def search(request: SearchRequest,service: SearchService = Depends(get_search_service)):
    """
    Search images by text or image.
    Search text -> convert to embedding -> query vectorDB -> get k best matching images -> return url
    """
    
    return service.search(request.query)
