import { defineStore } from 'pinia';
import { sendMessage, onMessage } from '../services/socket';

export const useChatStore = defineStore('chat', {
  state: () => ({
    messages: [],
  }),
  actions: {
    addMessage(message) {
      this.messages.push(message);
    },
    sendMessage(message) {
      sendMessage(message);
      this.addMessage({ user: 'You', content: message });
    },
  },
});

// Listen for incoming messages
onMessage((data) => {
  const chatStore = useChatStore();
  chatStore.addMessage(data);
});