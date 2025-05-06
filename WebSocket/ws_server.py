# ws_server.py
import asyncio
import websockets

async def handler(websocket):  # ⚠️ HANYA websocket, tanpa path!
    print("[Server] Menunggu data dari client...")
    async for message in websocket:
        print(f"[Server] Data diterima: {message} °C")
        await websocket.send(f"Server menerima suhu: {message} °C")

async def main():
    print("[Server] Menjalankan WebSocket server di ws://localhost:8765")
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())