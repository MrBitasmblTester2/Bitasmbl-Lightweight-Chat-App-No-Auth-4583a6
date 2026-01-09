# Bitasmbl-Lightweight-Chat-App-No-Auth-4583a6

## Description
Build a web application that allows users to join anonymous chatrooms and exchange messages in real-time using WebSockets. The focus is on fast communication, simple interface, and responsive updates without requiring user registration.

## Tech Stack
- FastAPI
- Vue.js
- Socket.IO

## Requirements
- Anonymous chatrooms
- Real-time messaging with WebSockets
- Simple interface
- Responsive updates
- No user registration

## Installation
bash
git clone https://github.com/MrBitasmblTester2/Bitasmbl-Lightweight-Chat-App-No-Auth-4583a6.git
cd Bitasmbl-Lightweight-Chat-App-No-Auth-4583a6

Backend:
bash
pip install fastapi uvicorn
pip install "python-socketio[client]"

Frontend:
bash
npm install


## Usage
Backend:
bash
uvicorn main:app --reload

Frontend:
bash
npm run dev


## Implementation Steps
1. Set up FastAPI app with Socket.IO server integration.
2. Define chatroom join and message events.
3. Broadcast messages to room participants.
4. Create Vue.js UI for room selection and messaging.
5. Connect Vue.js to Socket.IO server.
6. Handle real-time updates and message rendering.
7. Ensure no authentication or registration flows.

## API Endpoints
- WebSocket/Socket.IO namespace for chat connections