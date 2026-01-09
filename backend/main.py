import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
fastapi_app = FastAPI()
fastapi_app.add_middleware(CORSMiddleware, allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])

@fastapi_app.get("/health")
async def health():
    return {"status": "ok"}

app = socketio.ASGIApp(sio, other_asgi_app=fastapi_app)