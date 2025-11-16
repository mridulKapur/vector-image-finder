from fastapi import APIRouter, HTTPException, Query
from typing import List
import uuid
from .utils_image import iter_images
from .clip_model import embed_image
from .qdrant_client import upsert_points
from qdrant_client.models import PointStruct

router = APIRouter()

@router.post("/index")
async def index_folder(folder: str = Query(..., description="Absolute path to images folder")):
    try:
        print(folder)
        paths = list(iter_images(folder))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


    points = []
    for p in paths:
        try:
            vec = embed_image(p)
            pid = str(uuid.uuid4())
            payload = {"path": p, "filename": p.split('/')[-1]}
            points.append(PointStruct(id=pid, vector=vec, payload=payload))
        except Exception:
            # skip files that fail
            continue


    if points:
        upsert_points(points)


    return {"indexed": len(points)}