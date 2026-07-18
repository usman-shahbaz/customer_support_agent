import pickle

import faiss
import numpy as np

from config import (
    DOCUMENTS_PATH,
    FAISS_INDEX_PATH,
    TOP_K,
)

from embedding_client import get_embedding


class RAGEngine:

    def __init__(self):

        self.index = faiss.read_index(
            FAISS_INDEX_PATH
        )

        with open(
            DOCUMENTS_PATH,
            "rb",
        ) as f:
            self.documents = pickle.load(f)

    def retrieve(
        self,
        question,
        top_k=TOP_K,
    ):

        embedding = np.array(
            [get_embedding(question)],
            dtype="float32",
        )

        _, indices = self.index.search(
            embedding,
            top_k,
        )

        chunks = []

        for idx in indices[0]:

            if idx == -1:
                continue

            chunks.append(
                self.documents[idx]
            )

        return chunks

    def build_context(self, question):

        chunks = self.retrieve(question)

        return "\n\n".join(chunks)
