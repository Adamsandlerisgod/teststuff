<template>
	<div :class="messageClass">
		<strong class="username">{{ message.user }}</strong> 
		<span class="content">{{ message.content }}</span>
		<span class="timestamp">{{ message.timestamp }}</span>
	</div>
</template>

<script>
export default {
	props: ['message'],
	computed: {
		messageClass() {
			return {
				message: true,  // Base class
				'direct-message': this.message.content.startsWith('(DM'), // Highlight DMs
				'system-message': this.message.user.toLowerCase() === 'system', // Highlight system messages
			};
		}
	}
};
</script>

<style scoped>
/* General Message Styling */
.message {
	display: flex;
	flex-direction: column;
	background: #e1f5fe; /* Light blue for normal messages */
	padding: 10px;
	border-radius: 8px;
	margin-bottom: 10px;
	max-width: 75%;
}

/* Direct Messages */
.direct-message {
	background: #ffd54f; /* Yellow for direct messages */
	border-left: 5px solid #ff9800; /* Orange border for visibility */
}

/* System Messages */
.system-message {
	background: #d3d3d3; /* Gray for system messages */
	color: #333; /* Darker text for readability */
	font-style: italic;
	text-align: center;
	border-left: none;
	border-radius: 8px;
}

/* Username Styling */
.username {
	font-weight: bold;
	color: #2c3e50;
}

/* Message Content */
.content {
	color: #34495e;
}

/* Timestamp */
.timestamp {
	font-size: 0.8rem;
	color: gray;
	align-self: flex-end;
}
</style>
