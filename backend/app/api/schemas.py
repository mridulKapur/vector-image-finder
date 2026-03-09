from pydantic import BaseModel
from typing import List

class UploadInitResponse(BaseModel):
    upload_url: str
    image_id: str


class SearchRequest(BaseModel):
    query: str


class SearchResult(BaseModel):
    image_id: str
    score: float


class SearchResponse(BaseModel):
    results: List[SearchResult]
