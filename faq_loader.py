import docx
from app.core.qdrant_service import add_faqs_to_qdrant

def load_faqs_from_docx(docx_path: str):
    try:
        doc = docx.Document(docx_path)
    except Exception as e:
        print(f"Error loading DOCX file: {e}")
        return []
    faqs = []
    current_question = None 
    current_answer = [] 
    try:
        for para in doc.paragraphs:
            if para.text.strip():
                if para.text.strip().endswith('?'):
                    if current_question:
                        faqs.append({'question': current_question, 'answer': ' '.join(current_answer).strip()})
                    current_question = para.text.strip()
                    current_answer = []
                else:
                    current_answer.append(para.text.strip())
        if current_question:
            faqs.append({'question': current_question, 'answer': ' '.join(current_answer).strip()})
    except Exception as e:
        print(f"Error processing DOCX file: {e}")
    return faqs

def main():
    docx_path = "C:\\Users\\AIFA USER 102\\Downloads\\Be! Payments FAQ.docx"
    try:
        faqs = load_faqs_from_docx(docx_path)
        print(f"Loaded FAQs: {faqs}")  
        add_faqs_to_qdrant(faqs)
    except Exception as e:
        print(f"Error adding FAQs to Qdrant: {e}")

if __name__ == "__main__":
    main()