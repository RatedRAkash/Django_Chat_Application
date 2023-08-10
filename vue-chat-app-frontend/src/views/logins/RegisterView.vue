<template>
  <div class="bg-black">
    <div class="p-10 lg:p-20 text-center">
      <h1 class="text-3xl lg:text-6xl text-white">Register</h1>
    </div>

    <form @submit.prevent="register" class="lg:w-1/4 px-4 mx-auto">
      <div class="mb-5">
        <label class="text-white">Username</label>

        <input v-model="username" type="text" placeholder="Username" class="w-full mt-2 px-4 py-2 rounded-xl"/>
      </div>

      <div class="mb-5">
        <label class="text-white">Email</label>

        <input v-model="email" type="email" placeholder="Email" class="w-full mt-2 px-4 py-2 rounded-xl"/>
      </div>

      <div class="mb-5">
        <label class="text-white">Password</label>

        <input v-model="password1" type="password" placeholder="Password" class="w-full mt-2 px-4 py-2 rounded-xl"/>
      </div>

      <div class="mb-5">
        <label class="text-white">Confirm password</label>

        <input v-model="password2" type="password" placeholder="Confirm Password" class="w-full mt-2 px-4 py-2 rounded-xl"/>
      </div>

<!--      <div class="mb-5 p-4 rounded-xl bg-red-300 text-white">-->
<!--        <p>{{ error|escape }}</p>-->
<!--      </div>-->

      <button type="submit" class="px-5 py-3 mb-4 rounded-xl text-white bg-teal-800 hover:bg-teal-700">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      email: "",
      password1: "",
      password2: "",
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post("/api/v1/signup", {
          username: this.username,
          email: this.email,
          password1: this.password1,
          password2: this.password2,
        });
        console.log(response.data);

        this.$router.push('/login'); // Redirect to Login Page
      }

      catch (error) {
        console.error(error.response.data);
      }
    },
  },
};
</script>
