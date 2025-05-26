# backend.py
from fastapi import FastAPI, WebSocket
import asyncio

app = FastAPI()

connected_clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            await websocket.receive_text()  # Just keep connection open
    except:
        connected_clients.remove(websocket)

async def notify_clients(message: str):
    for client in connected_clients:
        await client.send_text(message)

# Endpoint to trigger notification from promotion
@app.post("/notify")
async def notify():
    await notify_clients("update")
    return {"message": "Notified all clients"}
