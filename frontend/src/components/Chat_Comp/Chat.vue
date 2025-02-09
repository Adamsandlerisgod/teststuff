<template>
	<div class="chat-container">
		<!-- User List -->
		<UserList 
			:currentUser="this.currentUser"
			:activeUsers="activeUsers" 
			@block-user="blockUser" 
			@view-profile="viewProfile" 
			@invite-to-game="inviteToGame" 
			@direct-message="directMessage"
		/>

		<!-- Chat Section -->
		<div class="chat-section">
			<ChatWindow :messages="messages" />
			
			<!-- Message Input -->
			<div class="message-input">
				<input v-model="newMessage" @keyup.enter="sendMessage" placeholder="Type a message..." />
				<button @click="sendMessage">Send</button>
			</div>
		</div>
	</div>
</template>

<script>
import ChatWindow from './ChatWindow.vue';
import UserList from './UserList.vue';
import { sendMessage, onMessage } from '../../services/socket';

export default {
	components: { ChatWindow, UserList },
	data() {
		return {
			messages: [],
			newMessage: '',
			activeUsers: [],
			blockedUsers: [],
			currentUser: this.currentUser,
		};
	},
	mounted() {
		onMessage((data) => {
			console.log("Received message:", data);
			if (data.type === 'user_list_update') {
				this.activeUsers = data.active_users;
			} 
			else if (data.type === 'chat_message' && !this.blockedUsers.includes(data.message.user)) {
				this.messages.push(data.message);
			}
			else if (data.type === 'user_info') {
				this.currentUser = data.username;
				console.log(data.username);
			}
		});
	},
	methods: {
		sendMessage() {
			if (this.newMessage.trim()) {
				console.log(this.newMessage);
				sendMessage(this.newMessage);
				this.newMessage = '';
			}
		},
		blockUser(user) {
			if (user == this.currentUser) {
				alert(`You cannot block yourself: ${user}.`);
			} else if (!this.blockedUsers.includes(user)) {
				this.blockedUsers.push(user);
				alert(`You have blocked ${user}.`);
			}
		},
		viewProfile(user) {
			alert(`Viewing profile of ${user}`);
		},
		inviteToGame(user) {
			alert(`Game invitation sent to ${user}!`);
			// Implement game invite logic if needed (e.g., socket event)
		},
		directMessage(user) {
			this.newMessage = `@${user} `;
		},
	},
};
</script>

<style scoped>
.chat-container {
display: flex;
gap: 20px;
padding: 20px;
background-color: #f4f4f4;
height: 90vh;
}


.chat-section {
flex: 1;
display: flex;
flex-direction: column;
}


.message-input {
display: flex;
gap: 10px;
padding: 10px;
background: white;
border-radius: 8px;
box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.1);
}


input {
flex: 1;
padding: 12px;
border-radius: 6px;
border: 1px solid #ccc;
}


button {
background: #3498db;
color: white;
padding: 12px 16px;
border: none;
border-radius: 6px;
cursor: pointer;
}


button:hover {
background: #2980b9;
}
</style>
