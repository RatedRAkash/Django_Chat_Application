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
        const response = await axios.post("/api/logout");
        console.log(response.data);
        // Clear the token from local storage or Vuex store
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
