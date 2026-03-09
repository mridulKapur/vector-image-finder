from fastapi import APIRouter
from ..schemas import UploadInitResponse

router = APIRouter()

@router.post("/init", response_model=UploadInitResponse)
def init_upload():
    """
    Returns a signed upload URL (later).
    """
    return {
        "upload_url": "TODO",
        "image_id": "TODO"
    }


@router.post("/complete")
def upload_complete(image_id: str):
    """
    Triggers indexing job.
    """
    return {"status": "queued", "image_id": image_id}
