<template>
  <div class="page-product">
    <div class="columns is-multiline">
      <div class="column is-9">
        <figure class="image mb-6">
          <img v-bind:src="product.get_image">
        </figure>
        <h1 class="is-size-4">{{product.name}}</h1>
        <p>{{product.description}}</p>
      </div>

      <div class="column is-3">
        <h2 class="subtitle">Information</h2>

        <p><strong>Price: </strong>{{product.price}} $</p>

        <div class="field has-addons mt-6">
          <div class="control">
            <input type="number" class="input" min="1" v-model="quantity">
          </div>

          <div class="control">
            <a class="button is-dark" @click="addToCart">Add to Cart</a>
          </div>
        </div>

      </div>

    </div>

  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import {toast, ToastPosition, ToastType} from 'bulma-toast'

export default {
  name: 'ProductView',
  components: {

  },
  data(){
    return {
      quantity:1,
      product: {}
    }
  },
  mounted() {
    this.getProduct()
  },
  methods:{
    // jehetu Loading dekhabo tai function ta ke `async` kore raklam
     async getProduct() {
      this.$store.commit('setIsLoading', true)

      const token = localStorage.getItem('jwt-token')
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      const category_slug = this.$route.params.category_slug
      const product_slug = this.$route.params.product_slug

       await axios
          .get(`api/v1/products/${category_slug}/${product_slug}`)
          .then(responseObj =>{
            this.product = responseObj.data
            console.log(responseObj)
            document.title =  this.product.name + '| DjangoChat'
          })
          .catch(errorObj =>{
            console.log(errorObj)
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