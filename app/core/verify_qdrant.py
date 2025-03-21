from qdrant_service import search_faq

def main():
    question = "How to apply for the card?"  
    results = search_faq(question)
    print("Search results:", results)

if __name__ == "__main__":
    main()