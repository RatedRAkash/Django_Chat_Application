<template>
  <div class="home">

    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
            Welcome to HomePage
        </p>
        <p class="subtitle">
            The Best Online Store
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>

  <!--  Start of v-FOR Loop -->
      <div class="column is-3"
        v-for="single_product in latestProducts"
           v-bind:title="single_product.id">

        <div class="box">
          <figure class="image mb-4">
            <img :src="single_product.get_thumbnail">
          </figure>
          <h3 class="is-size-4">{{single_product.name}}</h3>
          <p class="is-size-6 has-text-grey">{{single_product.price}}</p>

          <router-link v-bind:to="single_product.get_absolute_url" class="button is-dark mt-4">View Details</router-link>
        </div>

      </div>
  <!-- End of v-FOR Loop -->

    </div>

  </div>
</template>

<script>
// @ is an alias to /src

import axios from "axios";

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
    this.getLatestProducts()
  },
  methods:{
    getLatestProducts() {
      axios
          .get('api/v1/latest-products')
          .then(responseObj =>{
            this.latestProducts = responseObj.data
            console.log(responseObj)
          })
          .catch(errorObj =>{
            console.log(errorObj)
          })
    }
  }
}
</script>

<style scoped>
  .image{
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>