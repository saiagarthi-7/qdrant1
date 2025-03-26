from fastapi import FastAPI
from api import websocket_router
from core.qdrant_service import search_faq
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="FAQ Chatbot API")

app.include_router(websocket_router.router)

app.add_middleware(      
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FAQ Chatbot API"}

@app.get("/search")
def search(question: str):
    results = search_faq(question)
    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    