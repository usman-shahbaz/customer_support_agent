import os
import pickle
import faiss
import numpy as np

from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from embedding_client import get_embedding

from config import (
    DATA_DIR,
    VECTORSTORE_DIR,
    FAISS_INDEX_PATH,
    DOCUMENTS_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


def load_documents():

    text = ""

    for file in os.listdir(DATA_DIR):

        path = os.path.join(DATA_DIR, file)

        if file.lower().endswith(".pdf"):

            reader = PdfReader(path)

            for page in reader.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

        elif file.lower().endswith((".md", ".txt")):

            with open(path, "r", encoding="utf-8") as f:
                text += f.read() + "\n"

    return text


def split_documents(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    return splitter.split_text(text)


def build_vectorstore():

    text = load_documents()

    chunks = split_documents(text)

    embeddings = []

    for chunk in chunks:

        embeddings.append(get_embedding(chunk))

    embeddings = np.array(embeddings, dtype="float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])

    index.add(embeddings)

    os.makedirs(VECTORSTORE_DIR, exist_ok=True)

    faiss.write_index(index, FAISS_INDEX_PATH)

    with open(DOCUMENTS_PATH, "wb") as f:
        pickle.dump(chunks, f)

    print("Vector store created successfully.")


if __name__ == "__main__":
    build_vectorstore()
