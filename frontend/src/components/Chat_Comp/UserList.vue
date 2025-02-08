<template>
	<div class="user-list">
	<h3>Active Users</h3>
	<ul>
		<li v-for="user in activeUsers" :key="user" class="user-item">
		<span @click="showOptions(user)" class="username">{{ user }}</span>
		<div v-if="selectedUser === user" class="user-options">
			<button @click="blockUser(user)">🚫 Block</button>
			<button @click="viewProfile(user)">👤 View Profile</button>
		</div>
		</li>
	</ul>
	</div>
</template>

<script>
export default {
	props: ['activeUsers'],
	data() {
	return {
		selectedUser: null, // Track which user is clicked
	};
	},
	methods: {
	showOptions(user) {
		this.selectedUser = this.selectedUser === user ? null : user;
	},
	blockUser(user) {
		this.$emit('block-user', user);
		this.selectedUser = null; // Hide menu after action
	},
	viewProfile(user) {
		this.$emit('view-profile', user);
		this.selectedUser = null; // Hide menu after action
	},
	}
};
</script>

<style scoped>
.user-list {
	width: 250px;
	height: 400px;
	background-color: #4CAF50;
	color: white;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: flex-start;
	border-radius: 10px;
	font-size: 1.2rem;
	font-weight: bold;
	box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
	text-transform: uppercase;
	text-align: center;
	padding: 10px;
}

.user-item {
position: relative;
padding: 10px; /* Add some padding to the username area */
cursor: pointer;
}

.username {
color: #ffffff;
font-weight: bold;
cursor: pointer;
padding: 6px 10px; /* Add some padding to the username */
}

.username:hover {
text-decoration: underline;
}

.user-options {
  position: absolute;
  top: 50%; /* Vertically center the options relative to the username */
  left: 100%; /* Position the options just to the right of the username */
  transform: translateY(-50%); /* Center it vertically */
  background: white;
  border: 1px solid #ccc;
  border-radius: 6px;
  padding: 5px;
  display: flex;
  flex-direction: column;
  min-width: 120px; /* Increase width if needed */
  z-index: 10; /* Ensure the options are above the username */
}

.user-options button {
border: none;
background: none;
padding: 5px;
cursor: pointer;
text-align: left;
}

.user-options button:hover {
background: #f0f0f0;
}

</style>