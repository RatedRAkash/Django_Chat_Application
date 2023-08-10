<template>
  <div>
    <div class="bg-black">
      <div class="p-10 lg:p-20 text-center">
        <h1 class="text-3xl lg:text-6xl text-white">Logout</h1>
      </div>
      <button @click="logout" class="px-5 py-3 mb-4 rounded-xl text-white bg-teal-800 hover:bg-teal-700">Logout</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    async logout() {
      try {
        // Get BasicAuth from local storage
        const basicAuth = localStorage.getItem('basicAuth');
        axios.defaults.headers.common['Authorization'] = basicAuth;

        const response = await axios.post("/api/logout",{

        });
        console.log(response.data);

        localStorage.removeItem('basicAuth'); // Remove BasicAuth from local storage
        delete axios.defaults.headers.common['Authorization'];
        this.$router.push('/login'); // Redirect to Login Page

      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
