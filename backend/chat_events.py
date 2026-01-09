from typing import Dict, List
from .main import sio

rooms: Dict[str, List[dict]] = {}

@sio.event
async def connect(sid, environ):
    pass

@sio.event
async def join_room(sid, data):
    pass

@sio.event
async def send_message(sid, data):
    pass
