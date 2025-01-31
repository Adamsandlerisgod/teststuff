<template>
  <div class="chat">
    <ChatWindow :messages="messages" />
    <input v-model="newMessage" @keyup.enter="sendMessage" placeholder="Type a message..." />
  </div>
</template>

<script>
import ChatWindow from './ChatWindow.vue';
import { sendMessage } from '../../services/socket';

export default {
  components: { ChatWindow },
  data() {
    return {
      messages: [],
      newMessage: '',
    };
  },
  mounted() {
    // Listen for incoming messages
    this.socket = new WebSocket('ws://localhost:8000/ws/chat/');
    this.socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      this.messages.push(data);
    };
  },
  methods: {
    sendMessage() {
      if (this.newMessage.trim()) {
        sendMessage(this.newMessage);
        this.newMessage = '';
      }
    },
  },
};
</script>

<style scoped>
.chat {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

input {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-top: 10px;
}
</style>