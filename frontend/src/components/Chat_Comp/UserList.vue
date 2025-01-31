<template>
    <div class="user-list">
      <h3>Online Users</h3>
      <ul>
        <li v-for="user in users" :key="user.id">{{ user.username }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    props: ['users'],
  };
  </script>
  
  <style scoped>
  .user-list {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 10px;
    background-color: #fff;
    margin-left: 20px;
  }
  
  h3 {
    margin-top: 0;
  }
  </style>