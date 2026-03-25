from typing import Annotated
from fastapi import APIRouter, Depends, File, UploadFile

from app.api.dependencies import get_upload_service
from app.services.upload.service import UploadService
from ..schemas import UploadInitResponse

router = APIRouter()

@router.post("/upload", response_model=UploadInitResponse)
async def upload(
    file: UploadFile ,
    service: UploadService = Depends(get_upload_service),
):
    """
    Returns a signed upload URL (later).
     Upload image -> save image -> trigger indexing job -> return signed url job id and image id.
    """
    return await service.upload(file)
