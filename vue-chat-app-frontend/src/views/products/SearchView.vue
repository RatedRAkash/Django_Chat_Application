<template>
  <div class="page-search">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Search</h1>

        <h2 class="is-size-5 has-text-grey">Search term: "{{ query }}"</h2>
      </div>

      <!--  Start of v-FOR Loop -->
      <ProductBoxComponent
          v-for="single_product in productsList"
          v-bind:key="single_product.id"
          v-bind:product_obj="single_product">
      </ProductBoxComponent>
      <!-- End of v-FOR Loop -->

    </div>
  </div>
</template>

<script>
import axiosInstance from '@/axios.js'
import ProductBoxComponent from '@/components/ProductBoxComponent.vue'

export default {
  name: 'Search',
  components: {
    ProductBoxComponent
  },
  data() {
    return {
      productsList: [],
      query: ''
    }
  },
  mounted() {
    document.title = 'Search | DjangoChat'

    let uri = window.location.search.substring(1)
    let params = new URLSearchParams(uri)

    if(params.get('query')){
      this.query = params.get('query')

      this.performSearch()
    }
  },
  methods:{
    async performSearch(){
      this.$store.commit('setIsLoading', true)

      await axiosInstance
          .post(`api/v1/products/search`, {'query':this.query})
          .then(responseObj =>{
            this.productsList = responseObj.data
            console.log(responseObj)
          })
          .catch(errorObj =>{
            console.log(errorObj)
          })

      this.$store.commit('setIsLoading', false)

    }
  },
}
</script>