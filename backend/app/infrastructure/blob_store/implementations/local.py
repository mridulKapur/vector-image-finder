import shutil
import os,uuid
from pathlib import Path
from PIL import Image
from fastapi import UploadFile, HTTPException
from app.infrastructure.blob_store.base import StorageBackend

class LocalStorage(StorageBackend):

    def __init__(self):
        self.UPLOAD_DIR = Path("uploads")
        self.UPLOAD_DIR.mkdir(exist_ok=True)

    async def save_images(self, images: list[UploadFile]) -> list[str]:
        result = []
        for image in images:
            try:                
                image_id = uuid.uuid4()
                file_path = self.UPLOAD_DIR / f"{image_id}.jpg"
                with open(file_path, "wb") as buffer:
                    shutil.copyfileobj(image.file, buffer)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"There was an error uploading the file: {e}")
            finally:
                await image.close()

            result.append(str(image_id))
        return result

    def load_image(self, image_path: str):
        return Image.open(image_path).convert('RGB')
        
    def get_image_url(self, image_id:str):
        return str((self.UPLOAD_DIR / f"{image_id}.jpg").absolute())

    def get_image_metadata(self, image_url:str):
        return {"url":image_url,"id":os.path.basename(image_url)}