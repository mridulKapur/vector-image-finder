# embedding_model/factory.py
from base import EmbeddingModel
from implementations.clip_model import CLIPEmbeddingModel


_model_instance: EmbeddingModel | None = None


def get_embedding_model() -> EmbeddingModel:
    global _model_instance
    if _model_instance is None:
        _model_instance = CLIPEmbeddingModel()
    return _model_instance
