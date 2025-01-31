<template>
    <div class="message">
      <strong>{{ message.user }}:</strong> {{ message.content }}
    </div>
  </template>
  
  <script>
  export default {
    props: ['message'],
  };
  </script>
  
  <style scoped>
  .message {
    margin-bottom: 10px;
  }
  </style>