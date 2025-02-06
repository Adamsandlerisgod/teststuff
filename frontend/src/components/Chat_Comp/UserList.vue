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
  width: 250px; /* Make it bigger */
  height: 400px; /* Adjust the height */
  background-color: #4CAF50; /* Green background */
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  font-size: 1.5rem;
  font-weight: bold;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
  text-transform: uppercase;
  text-align: center;
}
</style>
