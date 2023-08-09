import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
      items: [],
    },
    isAuthenticated: false,
    token: '',
    isLoading: true
  },
  getters: {
  },

  // .commit(Synchronous kaaj kore sudhu)
  mutations: {
    initializeStore(state){
      if(localStorage.getItem('cart')){
        state.cart = JSON.parse(localStorage.getItem('cart'))
      }else{
        localStorage.setItem('cart', JSON.stringify(state.cart))
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
