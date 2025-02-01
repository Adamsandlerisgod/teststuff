<template>
  <div class="chat-window">
    <Message v-for="(message, index) in messages" :key="index" :message="message" />
  </div>
</template>

<script>
import Message from './Message.vue';

export default {
  components: { Message },
  props: ['messages'],
};
</script>
  
  <style scoped>
  .chat-window {
    flex: 1;
    overflow-y: auto;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: #fff;
  }
  
  .message {
    margin-bottom: 10px;
  }
  </style>