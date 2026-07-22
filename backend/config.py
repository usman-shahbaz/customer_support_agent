import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")

CHAT_MODEL_ID = os.getenv(
    "CHAT_MODEL_ID",
    "anthropic.claude-3-haiku-20240307-v1:0"
)

EMBEDDING_MODEL_ID = os.getenv(
    "EMBEDDING_MODEL_ID",
    "amazon.titan-embed-text-v2:0"
)

DATA_DIR = "data"
VECTORSTORE_DIR = "vectorstore"

FAISS_INDEX_PATH = os.path.join(VECTORSTORE_DIR, "faiss_index")
DOCUMENTS_PATH = os.path.join(VECTORSTORE_DIR, "documents.pkl")

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

TOP_K = 4
