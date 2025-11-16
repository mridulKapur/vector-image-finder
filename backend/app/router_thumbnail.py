# backend/app/router_thumbnail.py
from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import FileResponse
from PIL import Image
import os
import hashlib

router = APIRouter()

THUMB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "thumbnails")
THUMB_DIR = os.path.abspath(THUMB_DIR)
os.makedirs(THUMB_DIR, exist_ok=True)

def _thumb_path_for(src_path: str, size: int):
    # create a stable hashed filename to avoid collisions
    h = hashlib.sha1(src_path.encode("utf-8")).hexdigest()
    base = f"{h}_{size}.jpg"
    return os.path.join(THUMB_DIR, base)

@router.get("/thumbnail")
async def get_thumbnail(path: str = Query(..., description="Absolute image path on disk"),
                        size: int = Query(256, description="Max size in px")):
    if not os.path.isabs(path):
        raise HTTPException(status_code=400, detail="Path must be absolute")

    if not os.path.isfile(path):
        raise HTTPException(status_code=404, detail="File not found")

    out_path = _thumb_path_for(path, size)

    # if thumbnail exists and is newer than source, return it
    try:
        if os.path.exists(out_path):
            thumb_mtime = os.path.getmtime(out_path)
            src_mtime = os.path.getmtime(path)
            if thumb_mtime >= src_mtime:
                return FileResponse(out_path, media_type="image/jpeg")

        # create thumbnail
        with Image.open(path) as img:
            img.convert("RGB")
            img.thumbnail((size, size))
            img.save(out_path, format="JPEG", quality=85)
        return FileResponse(out_path, media_type="image/jpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
