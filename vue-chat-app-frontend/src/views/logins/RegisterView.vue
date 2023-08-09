<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <input v-model="username" placeholder="Username" />
      <input v-model="email" placeholder="Email" />
      <input v-model="password1" type="password" placeholder="Password" />
      <input v-model="password2" type="password" placeholder="Confirm Password" />
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "akash",
      email: "akash@gmail.com",
      password1: "akash123456",
      password2: "akash123456",
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post("http://localhost:7070/api/signup", {
          username: this.username,
          email: this.email,
          password: this.password1,
          // password2: this.password2,
        });
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
