<template>
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

  <div>
    <div class="column is-12">
      <h2 class="is-size-2 has-text-centered">Categories</h2>
    </div>

    <div class="column is-3"
         v-for="single_category in categoryList"
         v-bind:key="single_category.id">
      <div class="box">
        <h3 class="is-size-4">{{ single_category.name }}</h3>

        <router-link v-bind:to="`${single_category.slug}`"
                     class="button is-dark mt-4">Visit
        </router-link>
      </div>
    </div>

  </div>

</template>

<script>

// @ is an alias to /src
import axiosInstance from "@/axios.js";
import ProductBoxComponent from "@/components/ProductBoxComponent.vue";

export default {
  name: 'AllProducts',
  components: {
    ProductBoxComponent,
  },
  data() {
    return {
      latestProducts: [],
      categoryList: []
    }
  },
  mounted() {
    document.title = 'Products | DjangoChat'
    this.getLatestProducts()
    this.getAllCategories()
  },
  methods: {

    // jehetu Loading dekhabo tai function ta ke `async` kore raklam
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)
      await axiosInstance
          .get('api/v1/latest-products')
          .then(responseObj => {
            this.latestProducts = responseObj.data
            console.log(responseObj)
          })
          .catch(errorObj => {
            console.log(errorObj)
          })
      this.$store.commit('setIsLoading', false)
    },

    async getAllCategories() {
      this.$store.commit('setIsLoading', true)
      await axiosInstance
          .get('api/v1/categories')
          .then(responseObj => {
            this.categoryList = responseObj.data
            console.log(responseObj)
          })
          .catch(errorObj => {
            console.log(errorObj)
          })
      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>
