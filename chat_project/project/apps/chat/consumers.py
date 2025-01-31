import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Save message to the database
        await self.save_message(message)

        # Broadcast message to all connected clients
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def save_message(self, message):
        # Logic to save the message to the database
        pass