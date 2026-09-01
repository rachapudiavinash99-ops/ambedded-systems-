import asyncio
import random
import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()

@router.websocket("/ws/telemetry")
async def telemetry_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    # Initial state
    cpu = 10.0
    ram = 40.0
    battery = 100.0
    temp = 35.0
    
    try:
        while True:
            # Random walk for realism
            cpu = max(0, min(100, cpu + random.uniform(-15, 15)))
            ram = max(10, min(95, ram + random.uniform(-2, 2)))
            temp = max(25, min(95, temp + (cpu/100 * 5) - random.uniform(0, 3)))
            battery = max(0, battery - (cpu/100 * 0.05))
            
            data = {
                "cpu": cpu,
                "ram": ram,
                "battery": battery,
                "temp": temp,
                "sensors": {
                    "accel_x": random.uniform(-1.0, 1.0),
                    "accel_y": random.uniform(-1.0, 1.0),
                    "accel_z": random.uniform(9.0, 10.0),
                    "gyro_x": random.uniform(-0.5, 0.5)
                }
            }
            
            await websocket.send_json(data)
            await asyncio.sleep(1) # Stream 1 frame per second
            
    except WebSocketDisconnect:
        print("Client disconnected from telemetry stream")
