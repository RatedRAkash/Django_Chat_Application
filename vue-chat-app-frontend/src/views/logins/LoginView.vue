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
        const response = await axios.post("/api/login", {
          username: this.username,
          password: this.password,
        });
        // const authToken = response.data.token;
        const credentials = `${this.username}:${this.password}`;
        const encodedCredentials = btoa(credentials); // Encode credentials to Base64

        const basicAuth = `Basic ${encodedCredentials}`

        localStorage.setItem('basicAuth', basicAuth);

        // Set the Authorization header for all subsequent requests
        axios.defaults.headers.common['Authorization'] = basicAuth;

        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
