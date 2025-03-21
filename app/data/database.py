from qdrant_client import QdrantClient
from dotenv import load_dotenv
import os

#load environment variables from .env file
load_dotenv()

QDRANT_API_KEY = os.getenv("qdrant_key")
QDRANT_HOST = os.getenv("qdrant_host")

qdrant_client = QdrantClient(url=QDRANT_HOST, api_key=QDRANT_API_KEY)

def get_qdrant_client():
    return qdrant_client
