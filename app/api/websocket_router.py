from fastapi import APIRouter, WebSocket
from core.chatbot import generate_answer

router = APIRouter()

@router.websocket("/ws/faq")
async def websocket_endpoint(wbsock: WebSocket):
    await wbsock.accept()
    while True:
        query = await wbsock.receive_text()
        answer = generate_answer(query)
        await wbsock.send_text(answer)
