<template>
  <div>
    <h2>Logout</h2>
    <button @click="logout">Logout</button>
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

      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
