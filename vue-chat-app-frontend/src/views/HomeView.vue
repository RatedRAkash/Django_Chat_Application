<template>
  <div class="home">

    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
            Welcome to DjangoChat
        </p>
        <p class="subtitle">
            You can Chat in this site using Django Channels
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="is-size-2 has-text-centered">
          <router-link to="/rooms"
                       class="button is-dark mt-4 has-text-centered">Chat Now
          </router-link>
        </h1>
      </div>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src

import axiosInstance from "@/axios.js";

export default {
  name: 'HomeView',
  components: {
  },
  data(){
    return {
      latestProducts: []
    }
  },
  mounted() {
    document.title = 'Home | DjangoChat'
    this.getLatestProducts()
  },
  methods:{

    // jehetu Loading dekhabo tai function ta ke `async` kore raklam
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)
      await axiosInstance
          .get('api/v1/latest-products')
          .then(responseObj =>{
            this.latestProducts = responseObj.data
            console.log(responseObj)
          })
          .catch(errorObj =>{
            console.log(errorObj)
          })
      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>
