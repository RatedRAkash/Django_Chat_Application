import { createStore } from 'vuex'
import axiosInstance from "@/axios";

export default createStore({
  state: {
    cart: {
      items: [],
    },
    isAuthenticated: false,
    userInfo: null,
    token: '',
    user_data: null,
    isLoading: false,
  },
  getters: {
  },

  // .commit(Synchronous kaaj kore sudhu)
  mutations: {
    // `App.vue` er `created()` ee call disi... so, all time eita `initializeStore` call hobe
    initializeStore(state){
      if(localStorage.getItem('cart')){
        state.cart = JSON.parse(localStorage.getItem('cart'))
      }else{
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }
    },

    // setup JWT-headers to "axiosInstance"
    initializeAuth(state) {
      if (localStorage.getItem('user-info')) {
        // Parse the JSON string back to an object
        const storedUserInfo = JSON.parse(localStorage.getItem('user-info'))
        state.userInfo = storedUserInfo
        state.token = storedUserInfo.access
        state.user_data = storedUserInfo.user
        state.isAuthenticated = true
        axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${storedUserInfo.access}`;
      } else {
        state.userInfo = null
        state.token = ''
        state.user_data = null
        state.isAuthenticated = false
        axiosInstance.defaults.headers.common['Authorization'] = "";
      }
    },

    addToCart(state, item){
      const Exists = state.cart.items.filter(i => i.product.id === item.product.id)

      if(Exists.length>0){
        Exists[0].quantity = parseInt(Exists[0].quantity) + parseInt(item.quantity)
      }else{
        state.cart.items.push(item)
      }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },

    setIsLoading(state, loadingStatus){
      state.isLoading = loadingStatus
    },
  },

  // .dispatch(Asynchronous+Synchronous kaaj kore)
  actions: {
  },
  modules: {
  }
})
