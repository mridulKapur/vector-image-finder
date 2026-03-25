# embedding_model/implementations/clip_model.py
from typing import List
import clip
import torch
from PIL import Image

from ..base import EmbeddingModel
from app.core.config import CLIP_MODEL


class CLIPEmbeddingModel(EmbeddingModel):

    def __init__(self):
        self._device = "cuda" if torch.cuda.is_available() else "cpu"
        self._model = None
        self._preprocessor = None
        self._load_model()

    def _load_model(self):
        if self._model is None or self._preprocessor is None:
            self._model, self._preprocessor = clip.load(
                CLIP_MODEL,
                device=self._device
            )

    def embed_image(self,img: Image) -> List[float]:
        tensor = self._preprocessor(img).unsqueeze(0).to(self._device)
        with torch.no_grad():
            emb = self._model.encode_image(tensor)
            emb = emb / emb.norm(dim=1, keepdim=True)
        return emb.cpu().numpy()[0].tolist()

    def embed_images(self, images:List[Image.Image]) -> List[float]:
        embeddings = [self.embed_image(image) for image in images]
        return embeddings

    def embed_text(self, text: str) -> List[float]:
        tokens = clip.tokenize([text]).to(self._device)

        with torch.no_grad():
            emb = self._model.encode_text(tokens)
            emb = emb / emb.norm(dim=-1, keepdim=True)

        return emb.cpu().numpy()[0].tolist()
