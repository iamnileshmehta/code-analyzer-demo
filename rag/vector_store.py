import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

    def add(self, vector, meta):
        self.index.add(np.array([vector]).astype('float32'))
        self.metadata.append(meta)

    def search(self, query_vector, top_k=3):
        if self.index.ntotal == 0:
            return []       # no vector yet return empty list


        D, I = self.index.search(
            np.array([query_vector]).astype('float32'), top_k
        )

        valid_indices = [i for i in I[0] if i < len(self.metadata)]
        return [self.metadata[i] for i in valid_indices]

    
        