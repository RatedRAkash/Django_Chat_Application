<template>
  <div class="page-category">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="is-size-2 has-text-centered">{{category.name}}</h1>
      </div>

      <!--  Start of v-FOR Loop -->
      <ProductBoxComponent
          v-for="single_product in category.products"
          v-bind:key="single_product.id"
          v-bind:product_obj="single_product">
      </ProductBoxComponent>
      <!-- End of v-FOR Loop -->

    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import {toast, ToastPosition, ToastType} from 'bulma-toast'
import ProductBoxComponent from "@/components/ProductBoxComponent.vue";

export default {
  name: 'CategoryView',
  components: {
    ProductBoxComponent,
  },
  data(){
    return {
      quantity:1,
      category: {
        products: []
      }
    }
  },
  mounted() {
    this.getCategoryRelatedProducts()
  },

  // ************CATEGORY Tab switch korle jeno `getCategoryRelatedProducts` bar bar call dey********************
  watch: {
    // Dynamic Function, tai LifeCycle hook Call Automatic Call korbe Nah... taar jonno amra $route "WATCH" korbo... jodi sheita Change hui taile `getCategoryRelatedProducts()` call dibo Manually
    $route(to, from){
      if(to.name === 'Category'){
        this.getCategoryRelatedProducts()
      }
    }
  },
  // ********************************

  methods:{
    // jehetu Loading dekhabo tai function ta ke `async` kore raklam
    async getCategoryRelatedProducts() {
      this.$store.commit('setIsLoading', true)

      const category_slug = this.$route.params.category_slug

      await axios
          .get(`api/v1/products/${category_slug}`)
          .then(responseObj =>{
            this.category = responseObj.data
            console.log(responseObj)
            document.title =  this.category.name + '| DjangoChat'
          })
          .catch(errorObj =>{
            console.log(errorObj)

            toast({
              message: 'Something went wrong. Please Try Again',
              type: 'is-danger',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'bottom-right',
            })

          })

      this.$store.commit('setIsLoading', false)
    },

    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1
      }
      const item = {
        product: this.product,
        quantity: this.quantity
      }

      this.$store.commit('addToCart', item)

      toast({
        message: 'The product was added to the cart',
        type: 'is-success',
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: 'bottom-right',
      })
    },
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