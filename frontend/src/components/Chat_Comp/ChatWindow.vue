<template>
    <div class="chat-window">
      <div v-for="(message, index) in messages" :key="index" class="message">
        <strong>{{ message.user }}:</strong> {{ message.content }}
      </div>
    </div>
  </template>
  
  <script>
  export default {
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