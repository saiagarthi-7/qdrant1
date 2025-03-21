from fastapi import APIRouter, WebSocket
from core.qdrant_service import search_faq

router = APIRouter()

@router.websocket("/ws/faq")
async def websocket_endpoint(wbsock: WebSocket):
    await wbsock.accept()
    while True:
        data = await wbsock.receive_text()
        results = search_faq(data)
        await wbsock.send_json(results)
