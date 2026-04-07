import faiss
import os
import numpy as np
from config import FAISS_PATH, EMBEDDING_DIM

def load_index():
    if os.path.exists(FAISS_PATH):
        return faiss.read_index(FAISS_PATH)
    return faiss.IndexFlatL2(EMBEDDING_DIM)

def save_index(index):
    faiss.write_index(index, FAISS_PATH)

class VectorStore:
    def __init__(self):
        self.index = load_index()

    def add(self, vector: np.ndarray) -> int:
        idx = self.index.ntotal
        self.index.add(vector.reshape(1, -1))
        save_index(self.index)
        return idx

    def search(self, vector: np.ndarray, k: int):
        if self.index.ntotal == 0:
            return []
        _, ids = self.index.search(vector.reshape(1, -1), k)
        return ids[0].tolist()
