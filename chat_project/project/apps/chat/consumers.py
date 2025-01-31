import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from project.apps.chat.models import ChatMessage 


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the room name from the URL
        self.room_name = 'chatroom'  # Default or dynamic room name
        self.room_group_name = f'chat_{self.room_name}'

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Parse the received message
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Save the message to the database
        await self.save_message(message)

        # Broadcast the message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # Send message to WebSocket
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def save_message(self, message):
        # Logic to save the message to the database
        # Assuming you have a ChatMessage model
        await database_sync_to_async(self._save_message)(message)

    def _save_message(self, message):
        # This is a synchronous function to interact with the database
        # Django's ORM is synchronous, so we need to wrap it with database_sync_to_async
        ChatMessage.objects.create(content=message, string='guest')

