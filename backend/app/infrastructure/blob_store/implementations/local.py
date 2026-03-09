import os
from PIL import Image

from app.infrastructure.blob_store.base import StorageBackend, ImageData
from app.utils.utils_image import iter_images

class LocalStorage(StorageBackend):

    def load_images(self, folder_path: str):
        images = []

        for file in os.listdir(folder_path):
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                full_path = os.path.join(folder_path, file)
                images.append(
                    Image.open(full_path).convert('RGB')
                )

        return images

    def get_images_metadata(self, folder_path:str):
        paths = iter_images(folder=folder_path)
        return [{"path":p,"filename":p.split('/')[-1]} for p in paths]