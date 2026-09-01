from fastapi import WebSocket

async def telemetry_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"cpu": 45.2, "battery": 88})
