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
import axiosInstance from "@/axios.js";

export default {
  methods: {
    async logout() {
      try {
        const response = await axiosInstance.post("/api/v1/logout",{

        });
        console.log(response.data);

        // localStorage.removeItem('basicAuth'); // Remove BasicAuth from local storage
        localStorage.removeItem('user-info');

        delete axiosInstance.defaults.headers.common['Authorization'];
        this.$router.push('/login'); // Redirect to Login Page

      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
