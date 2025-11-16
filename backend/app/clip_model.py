import clip
import torch
from PIL import Image
from typing import List
from .config import CLIP_MODEL

_device = "cuda" if torch.cuda.is_available() else "cpu"
_model = None
_preprocessor = None

def load_model():
    global _model,_preprocessor
    if _model is None or _preprocessor is None:
        _model,_preprocessor = clip.load(CLIP_MODEL,device=_device)
    return _model,_preprocessor

def embed_image(path:str) -> List[float]:
    model,preprocessor = load_model()
    img = Image.open(path).convert("RGB")
    tensor = preprocessor(img).unsqueeze(0).to(_device)
    with torch.no_grad():
        emb = model.encode_image(tensor)
        emb = emb / emb.norm(dim=1,keepdim=True)
    finalList = emb.cpu().numpy()[0].tolist()
    return finalList

def embed_text(text: str) -> List[float]:
    model, _ = load_model()
    tokens = clip.tokenize([text]).to(_device)
    with torch.no_grad():
        emb = model.encode_text(tokens)
        emb = emb / emb.norm(dim=-1, keepdim=True)
    return emb.cpu().numpy()[0].tolist()