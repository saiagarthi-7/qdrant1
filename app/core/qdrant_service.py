from qdrant_client.models import VectorParams, Distance, PointStruct
from core.embeddings import get_embedding
from data.database import get_qdrant_client

qdrant = get_qdrant_client()
COLLECTION_NAME = "faq2_collection"

def create_collection_if_not_exists():
    try:
        collections = qdrant.get_collections().collections
        if COLLECTION_NAME not in [col.name for col in collections]:
            qdrant.recreate_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(size=384, distance=Distance.COSINE)
            )
        print('Collection created or already exists')  # Debug statement
    except Exception as e:
        print(f"Error creating collection: {e}")

def add_faqs_to_qdrant(faqs: list):
    try:
        create_collection_if_not_exists()
        points = []
        for i, qa in enumerate(faqs):
            try:
                vector = get_embedding(qa['question'])
                print(f"Generated vector for question {i}: {vector}")  
                points.append(PointStruct(id=i, vector=vector, payload=qa))
            except Exception as e:
                print(f"Error generating vector for question {i}: {e}")
        print(len(points))  
        print(points)
        qdrant.upsert(collection_name=COLLECTION_NAME, points=points)
        print(f"Added points to Qdrant: {points}")  
    except Exception as e:
        print(f"Error adding FAQs to Qdrant: {e}")

def search_faq(question: str, top_k: int = 3):
    try:
        create_collection_if_not_exists()
        vector = get_embedding(question)
        print(f"Search vector: {vector}")  
        results = qdrant.search(collection_name=COLLECTION_NAME, query_vector=vector, limit=top_k)
        print(f"Search results: {results}")  
        return results
    except Exception as e:
        print(f'Error searching FAQs: {e}')
        return []