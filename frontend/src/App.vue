<template>
  <div id="app">
    <Chat />
  </div>
</template>

<script>
import Chat from './components/Chat_Comp/Chat.vue'; // Correct import path

export default {
  name: 'App',
  components: {
    Chat,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>