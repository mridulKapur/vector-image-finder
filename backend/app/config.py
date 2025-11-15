import os
from dotenv import load_dotenv
load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION", "photos")
EMBED_DIM = int(os.getenv("EMBED_DIM", "512"))

CLIP_MODEL = "ViT-B/32"

