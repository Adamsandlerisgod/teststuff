<template>
	<div class="user-list">
	<h3>Active Users</h3>
	<ul>
		<li v-for="user in activeUsers" :key="user" class="user-item">
		<span
			@click="showOptions(user)"
			:class="usernameClass(user)"
		>
			{{ user }}
		</span>
		<div v-if="selectedUser === user && user !== currentUser" class="user-options">
			<button @click="blockUser(user)">🚫 Block</button>
			<button @click="viewProfile(user)">👤 View Profile</button>
			<button @click="inviteToGame(user)">🎮 Invite to Game</button>
			<button @click="directMessage(user)">💬 Direct Message</button>
		</div>
		</li>
	</ul>
	</div>
</template>

<script>
export default {
	props: ['activeUsers', 'currentUser'],
	data() {
	return {
		selectedUser: null, // Track which user is clicked
	};
	},
	computed: {
	// Computed property to determine the class based on the user
	usernameClass() {
		return (user) => {
		return {
			'username': true, // Always apply the 'username' class
			'current-user': user === this.currentUser, // Apply 'current-user' if it's the current user
		};
		};
	}
	},
	methods: {
	showOptions(user) {
		if (user !== this.currentUser) {
		this.selectedUser = this.selectedUser === user ? null : user;
		} else {
		this.selectedUser = null;
		}
	},
	blockUser(user) {
		this.$emit('block-user', user);
		this.selectedUser = null;
	},
	viewProfile(user) {
		this.$emit('view-profile', user);
		this.selectedUser = null;
	},
	inviteToGame(user) {
		this.$emit('invite-to-game', user);
		alert(`Game invitation sent to ${user}!`);
		this.selectedUser = null;
	},
	directMessage(user) {
		this.$emit('direct-message', user);
		this.selectedUser = null;
	},
	},
};
</script>

<style scoped>
.user-list {
	width: 250px;
	height: 400px;
	background-color: #4caf50;
	color: white;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: flex-start;
	border-radius: 10px;
	font-size: 1.2rem;
	font-weight: bold;
	box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
	text-align: center;
	padding: 10px;
}

.user-item {
	position: relative;
	padding: 10px;
	cursor: pointer;
}

.username {
	color: #ffffff;
	font-weight: bold;
	cursor: pointer;
	padding: 6px 10px;
}

.username:hover {
	text-decoration: underline;
}

.username.current-user {
	color: #ffcc00;  /* Change color for current user */
}

.user-options {
	position: absolute;
	top: 50%;
	left: 100%;
	transform: translateY(-50%);
	background: white;
	border: 1px solid #ccc;
	border-radius: 6px;
	padding: 5px;
	display: flex;
	flex-direction: column;
	min-width: 150px;
	z-index: 10;
}

.user-options button {
	border: none;
	background: none;
	padding: 5px;
	cursor: pointer;
	text-align: left;
	width: 100%;
}

.user-options button:hover {
	background: #f0f0f0;
}
</style>
