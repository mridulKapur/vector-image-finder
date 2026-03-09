from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.domain.indexing.service import IndexingService
from app.api.dependencies import get_indexing_service

router = APIRouter(prefix="/index", tags=["index"])

class IndexRequest(BaseModel):
    folder_path: str

class IndexResponse(BaseModel):
    indexed_count: int

@router.post("", response_model=IndexResponse)
def index_images(
    request: IndexRequest,
    service: IndexingService = Depends(get_indexing_service),
):
    count = service.index_folder(request.folder_path)
    return IndexResponse(indexed_count=count)
