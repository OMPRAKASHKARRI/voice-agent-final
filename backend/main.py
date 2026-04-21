from fastapi import FastAPI, WebSocket
from backend.websocket.handler import websocket_handler

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Voice AI Agent Running"}

@app.websocket("/ws")
async def ws(ws: WebSocket):
    await websocket_handler(ws)