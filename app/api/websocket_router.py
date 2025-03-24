from fastapi import APIRouter, WebSocket,WebSocketDisconnect
from core.chatbot import generate_answer

router = APIRouter()

@router.websocket("/ws/faq")
async def websocket_endpoint(wbsock: WebSocket):
    await wbsock.accept()
    try:
        while True:
            query = await wbsock.receive_text()
            answer = generate_answer(query)
            await wbsock.send_text(answer)
    except WebSocketDisconnect:
        print("Client disconnected")
