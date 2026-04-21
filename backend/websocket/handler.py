from fastapi import WebSocket, WebSocketDisconnect
import uuid

from backend.agent.orchestrator import process_request


async def websocket_handler(ws: WebSocket):
    await ws.accept()

    session_id = str(uuid.uuid4())

    try:
        while True:
            message = await ws.receive()

            text = message.get("text")

            if not text:
                continue

            print("USER:", text)

            response = process_request(text, session_id)

            print("AI:", response)

            await ws.send_json({
                "text": response
            })

    except WebSocketDisconnect:
        print("🔌 Client disconnected")

    except Exception as e:
        print("❌ Error:", e)