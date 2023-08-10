<template>
  <div>
    <div class="bg-black">
      <div class="p-10 lg:p-20 text-center">
        <h1 class="text-3xl lg:text-6xl text-white">Login</h1>
      </div>

      <form @submit.prevent="login" class="lg:w-1/4 px-4 mx-auto">
        <div class="mb-5">
          <label class="text-white">Username</label>

          <input v-model="username" type="text" placeholder="Username" class="w-full mt-2 px-4 py-2 rounded-xl"/>
        </div>

        <div class="mb-5">
          <label class="text-white">Password</label>

          <input v-model="password" type="password" placeholder="Password" class="w-full mt-2 px-4 py-2 rounded-xl"/>
        </div>

        <button type="submit" class="px-5 py-3 mb-4 rounded-xl text-white bg-teal-800 hover:bg-teal-700">Submit</button>
      </form>
    </div>
<!--    <form @submit.prevent="login">-->
<!--      <input v-model="username" placeholder="Username" />-->
<!--      <input v-model="password" type="password" placeholder="Password" />-->
<!--      <button type="submit">Login</button>-->
<!--    </form>-->
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
        // const response = await axios.post("/api/login", {
        //   username: this.username,
        //   password: this.password,
        // });
        // // const authToken = response.data.token;
        // const credentials = `${this.username}:${this.password}`;
        // const encodedCredentials = btoa(credentials); // Encode credentials to Base64
        //
        // const basicAuth = `Basic ${encodedCredentials}`
        //
        // localStorage.setItem('basicAuth', basicAuth);
        //
        // // Set the Authorization header for all subsequent requests
        // axios.defaults.headers.common['Authorization'] = basicAuth;

        // console.log(response.data);

        const jwt_response = await axios.post("/api/gettoken", {
          username: this.username,
          password: this.password,
        });

        // localStorage.setItem('jwt-access-token', jwt_response.data.access);
        // localStorage.setItem('jwt-refresh-token', jwt_response.data.refresh);
        localStorage.setItem('user-info', JSON.stringify(jwt_response.data));
        console.log(jwt_response.data);

        // Set the Authorization header for all subsequent requests
        axios.defaults.headers.common['Authorization'] = `Bearer ${jwt_response.data.access}`;

        this.$router.push('/'); // Redirect to HOME Page

      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
