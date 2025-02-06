<!-- <template>
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
  </style> -->

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
    padding: 15px;
    border-radius: 10px;
    background: white;
    box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.1);
    max-height: 70vh;
  }
  </style>
  