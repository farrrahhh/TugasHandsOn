# ws_client.py
import asyncio
import websockets
import random

async def send_temperature():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        for _ in range(5):
            suhu = round(random.uniform(25.0, 35.0), 2)
            await websocket.send(str(suhu))
            print(f"[Client] Mengirim suhu: {suhu} °C")
            response = await websocket.recv()
            print(f"[Client] Respon server: {response}")
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(send_temperature())