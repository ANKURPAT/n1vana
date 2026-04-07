import numpy as np
from config import EMBEDDING_DIM

def embed(text: str) -> np.ndarray:
    rng = np.random.default_rng(abs(hash(text)) % (2**32))
    return rng.random(EMBEDDING_DIM).astype("float32")
