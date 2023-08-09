<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post("/api/token_obtain_pair", {
          username: this.username,
          password: this.password,
        });
        console.log(response.data);
        // You can store the token in local storage or Vuex store for future API calls
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
