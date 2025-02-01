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
        print("Received raw text_data:", repr(text_data))  # Debugging: Show raw message

        try:
            text_data_json = json.loads(text_data)
            message_content = text_data_json.get('message', '')
            print("Parsed message:", repr(message_content))
        except json.JSONDecodeError as e:
            print("JSON Decode Error:", e)
            return

        if not message_content:
            print("Empty or malformed message received.")
            return

        await self.save_message(message_content)
        # saved_message = await self.save_message(message_content)

        print("Message saved successfully.")

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                # 'type': 'chat_message',
                # 'message': saved_message
                'type' : 'chat_message',
                'message': message_content
            }
        )


    async def chat_message(self, event):
        message = event.get('message', 'ERROR: Missing message')
        print("Broadcasting message:", repr(message))

        await self.send(text_data=json.dumps({
            'message': message
            # 'content': message['content'],  # Include content in the message
            # 'user': message['user']  # Include user in the message
        }))


    async def save_message(self, message):
        # Logic to save the message to the database
        # Assuming you have a ChatMessage model
        await database_sync_to_async(self._save_message)(message)

    def _save_message(self, message):
        # This is a synchronous function to interact with the database
        # Django's ORM is synchronous, so we need to wrap it with database_sync_to_async
        from django.contrib.auth.models import User
        guest_user, _ = User.objects.get_or_create(username="guest", defaults={"password": "guestpassword"})
        print("message in saved message")
        print(guest_user.username)
        ChatMessage.objects.create(content=message, user=guest_user)


