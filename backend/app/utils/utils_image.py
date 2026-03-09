from PIL import Image
import os

VALID_EXT = {'.jpg', '.jpeg', '.png', '.webp', '.bmp'}

def is_image_file(path: str) -> bool:
    _, ext = os.path.splitext(path.lower())
    return ext in VALID_EXT

def iter_images(folder: str):
    for root, dirs, files in os.walk(folder):
        for f in files:
            path = os.path.join(root, f)
            if is_image_file(path):
                yield path