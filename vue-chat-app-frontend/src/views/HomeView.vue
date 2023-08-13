<template>
  <div class="home">

    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
            Welcome to HomePage
        </p>
        <p class="subtitle">
            You can Chat in this site using Django Channels
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>

  <!--  Start of v-FOR Loop -->
      <ProductBoxComponent
        v-for="single_product in latestProducts"
           v-bind:key="single_product.id"
           v-bind:product_obj="single_product">
      </ProductBoxComponent>
  <!-- End of v-FOR Loop -->

    </div>

  </div>
</template>

<script>
// @ is an alias to /src

import axiosInstance from "@/axios.js";
import ProductBoxComponent from "@/components/ProductBoxComponent.vue";

export default {
  name: 'HomeView',
  components: {
    ProductBoxComponent,
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
