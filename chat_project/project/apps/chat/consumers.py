import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from project.apps.chat.models import ChatMessage
from django.contrib.auth.models import User

# Store active users as a global dictionary (in-memory)
active_users = set()

class ChatConsumer(AsyncWebsocketConsumer):

	async def connect(self):
		self.room_name = 'chatroom'  
		self.room_group_name = f'chat_{self.room_name}'

		# Determine username (authenticated or guest)
		user = self.scope['user']
		if user.is_authenticated:
			username = user.username
		else:
			username = f"Guest-{self.channel_name[-5:]}"  # Unique guest ID
		
		self.username = username  # Store for disconnect handling

		# Add user to active list
		active_users.add(username)

		# Join group and accept connection
		await self.channel_layer.group_add(self.room_group_name, self.channel_name)
		await self.accept()

		# Send updated user list and a join message
		await self.send_user_list(event_type="join", username=self.username)

	async def disconnect(self, close_code):
		# Remove user from active list
		active_users.discard(self.username)

		# Leave the room group
		await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

		# Send updated user list and a leave message
		await self.send_user_list(event_type="leave", username=self.username)

	async def receive(self, text_data):
		print("Received raw text_data:", repr(text_data))  # Debugging

		try:
			text_data_json = json.loads(text_data)
			message_content = text_data_json.get('message', '')
		except json.JSONDecodeError as e:
			print("JSON Decode Error:", e)
			return

		if not message_content:
			print("Empty or malformed message received.")
			return

		saved_message = await self.save_message(message_content)

		await self.channel_layer.group_send(
			self.room_group_name,
			{
				'type': 'chat_message',
				'message': {
					'id': saved_message.id,
					'content': saved_message.content,
					'user': saved_message.user.username,
					'timestamp': saved_message.timestamp.isoformat(),
				}
			}
		)

	async def chat_message(self, event):
		await self.send(text_data=json.dumps({
			'type': 'chat_message',
			'message': event['message'],
		}))

	async def user_list_update(self, event):
		"""Receive and forward updated user list."""
		await self.send(text_data=json.dumps({
			'type': 'user_list_update',
			'active_users': event.get('active_users', []),
		}))

	async def send_user_list(self, event_type="update", username=None):
	# """Send the updated active user list and broadcast join/leave messages."""
		message = None

		if event_type == "join" and username:
			message = f"🔹 {username} has entered the chatroom."
		elif event_type == "leave" and username:
			message = f"🔸 {username} has left the chatroom."

		# Notify all clients of the updated user list
		await self.channel_layer.group_send(
			self.room_group_name,
			{
				"type": "user_list_update",
				"active_users": list(active_users),
			}
		)

		# If it's a join/leave message, send it as a chat event
		if message:
			await self.channel_layer.group_send(
				self.room_group_name,
				{
					"type": "chat_message",
					"message": {
						"id": None,  # No DB ID for system messages
						"content": message,
						"user": "System",  # System user
						"timestamp": None,  # No timestamp needed
					}
				}
			)


	@database_sync_to_async
	def save_message(self, message):
		guest_user, _ = User.objects.get_or_create(username=self.username, defaults={"password": "guestpassword"})
		return ChatMessage.objects.create(content=message, user=guest_user)


# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async
# from project.apps.chat.models import ChatMessage
# from django.contrib.auth.models import User

# class ChatConsumer(AsyncWebsocketConsumer):
# 	def __init__(self, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
# 		# Initialize active_users as an instance-level variable
# 		self.active_users = {}

# 	async def connect(self):
# 		# Get the room name from the URL
# 		self.room_name = 'chatroom'  # Default or dynamic room name
# 		self.room_group_name = f'chat_{self.room_name}'

# 		# Add user to active users list
# 		user = self.scope['user']
# 		# if user.is_authenticated:
# 		self.active_users[user.username] = {
# 			'username': user.username,
# 			'id': user.id,
# 		}

# 		# Join the room group
# 		await self.channel_layer.group_add(
# 			self.room_group_name,
# 			self.channel_name
# 		)

# 		# Accept the WebSocket connection
# 		await self.accept()

# 		# Notify all users in the room about the new user
# 		await self.channel_layer.group_send(
# 			self.room_group_name,
# 			{
# 				'type': 'user_list_update',
# 				'active_users': list(self.active_users.values()),
# 			}
# 		)

# 	async def disconnect(self, close_code):
# 		# Remove user from active users list
# 		user = self.scope['user']
# 		# if user.is_authenticated and user.username in self.active_users:
# 		del self.active_users[user.username]

# 		# Notify all users in the room about the user leaving
# 		await self.channel_layer.group_send(
# 			self.room_group_name,
# 			{
# 				'type': 'user_list_update',
# 				'active_users': list(self.active_users.values()),
# 			}
# 		)

# 		# Leave the room group
# 		await self.channel_layer.group_discard(
# 			self.room_group_name,
# 			self.channel_name
# 		)

# 	async def receive(self, text_data):
# 		print("Received raw text_data:", repr(text_data))  # Debugging: Show raw message

# 		try:
# 			text_data_json = json.loads(text_data)
# 			message_content = text_data_json.get('message', '')
# 			print("Parsed message:", repr(message_content))
# 		except json.JSONDecodeError as e:
# 			print("JSON Decode Error:", e)
# 			return

# 		if not message_content:
# 			print("Empty or malformed message received.")
# 			return

# 		# Save the message to the database
# 		saved_message = await self.save_message(message_content)

# 		print("Message saved successfully.")

# 		# Broadcast the message to the room
# 		await self.channel_layer.group_send(
# 			self.room_group_name,
# 			{
# 				'type': 'chat_message',
# 				'message': {
# 					'id': saved_message.id,
# 					'content': saved_message.content,
# 					'user': saved_message.user.username,
# 					'timestamp': saved_message.timestamp.isoformat(),
# 				}
# 			}
# 		)

# 	async def chat_message(self, event):
# 		message = event.get('message', 'ERROR: Missing message')
# 		print("Broadcasting message:", repr(message))

# 		await self.send(text_data=json.dumps({
# 			'type': 'chat_message',
# 			'message': message,
# 		}))

# 	async def user_list_update(self, event):
# 		print("Received event:", event)  # Debugging

# 		await self.send(text_data=json.dumps({
# 			'type': 'user_list_update',
# 			'active_users': event.get('active_users', []),  # Default to an empty list if missing
# 		}))


# 	@database_sync_to_async
# 	def save_message(self, message):
# 		guest_user, _ = User.objects.get_or_create(username="guest", defaults={"password": "guestpassword"})
# 		return ChatMessage.objects.create(content=message, user=guest_user)