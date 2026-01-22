from fastapi import APIRouter, HTTPException, Query
import uuid

from ...app.utils_image import iter_images

from ...models.factory import get_embedding_model
from ...store.factory import get_vector_store


router = APIRouter()
store = get_vector_store()
model = get_embedding_model()

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
            vec = model.embed_image(p)
            pid = str(uuid.uuid4())
            payload = {"path": p, "filename": p.split('/')[-1]}
            points.append({
                "id": pid,
                "vector": vec,
                "payload": payload
            })
        except Exception:
            # skip files that fail
            continue


    if points:
        store.upsert_points(points)


    return {"indexed": len(points)}