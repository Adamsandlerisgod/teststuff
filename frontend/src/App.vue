<template>
  <div id="app">
    <h1>Chat Application</h1>
    <Chat />
  </div>
</template>

<script>
import Chat from './components/Chat_Comp/Chat.vue';

export default {
  components: { Chat },
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
  margin-top: 20px;
}
</style>