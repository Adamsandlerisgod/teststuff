
  <template>
    <div class="message">
      <strong class="username">{{ message.user }}</strong> 
      <span class="content">{{ message.content }}</span>
      <span class="timestamp">{{ message.timestamp }}</span>
    </div>
  </template>
  
  <script>
  export default {
    props: ['message'],
  };
  </script>
  
  <style scoped>
  .message {
    display: flex;
    flex-direction: column;
    background: #e1f5fe;
    padding: 10px;
    border-radius: 8px;
    margin-bottom: 10px;
    max-width: 75%;
  }
  
  .username {
    font-weight: bold;
    color: #2c3e50;
  }
  
  .content {
    color: #34495e;
  }
  
  .timestamp {
    font-size: 0.8rem;
    color: gray;
    align-self: flex-end;
  }
  </style>
  