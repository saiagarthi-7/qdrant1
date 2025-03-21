from core.qdrant_service import search_faq

def generate_answer(query: str):
    results = search_faq(query)
    if results:
        top = results[0].payload
        return f"Q: {top['question']}\nA: {top['answer']}"
    return "Sorry, I couldn't find a relevant answer."