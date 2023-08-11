<template>
  <div id="wrapper">
  <nav class="navbar is-dark">

    <div class="navbar-brand">
      <router-link to="/" class="navbar-item"><strong>Home</strong></router-link>    <!-- Normal `href` Tag use nah kore...`router-link` TAG ta use korle VUE shei Request ke intercept kore and nijei shei route ee niye jabe without Network Call to SERVER -->
      <a class="navbar-burger" @click="showMobileMenu = !showMobileMenu" aria-label="menu" aria-expanded="false" data-target="navbar-menu">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">

      <!--     SEARCH BUTTON -->
      <div class="navbar-start">
        <div class="navbar-item">

          <!--    eikane action="/search" VUE er Route ke Point kortese... kono BACKEND er URL ke NAH -->
          <form method="get" action="/search">
            <div class="field has-addons">
              <div class="control">
                <input type="text" class="input" placeholder="What are you looking for?" name="query"> <!-- eikane name="query" dewa... mane FORM Submit korle "{BASE_URL}/?name=..." eivabe boshbe -->
              </div>

              <div class="control">
                <button class="button is-success">
                      <span class="icon">
                      <i class="fas fa-search"></i>
                      </span>
                </button>
              </div>
            </div>
          </form>

        </div>
      </div>

      <!--     HAMBURGER MENU -->
      <div class="navbar-end">
        <router-link to="/summer" class="navbar-item">Summer</router-link>
        <router-link to="/winter" class="navbar-item">Winter</router-link>
        <router-link to="/rooms" class="navbar-item">Rooms</router-link>

        <div class="navbar-item">
          <div class="buttons">
            <router-link to="/login" class="button is-light">Log In</router-link>
            <router-link to="/signup" class="button is-light">Sign Up</router-link>
            <router-link to="/logout" class="button is-light">Log Out</router-link>

            <router-link to="/cart" class="button is-success">
              <span class="icon"><i class="fas fa-shopping-cart"></i></span>
              <span>Cart ({{cartTotalLength}})</span>
            </router-link>
          </div>
        </div>
      </div>

    </div>
  </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
      <!-- `router-view` TAG ta jei Route ee gese shei Route er COMPONENT ke automatic Import korte pari tik ei Jaigai -->
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (Akash) 2023</p>
    </footer>

  </div>

</template>

<script>

import axiosInstance from "@/axios";

export default {
  name: 'App',
  components: {
  },
  data(){
    return {
      showMobileMenu: false,
      cart:{
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (localStorage.getItem('user-info')) {
      // Parse the JSON string back to an object
      const storedUserInfo = JSON.parse(localStorage.getItem('user-info'))
      axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${storedUserInfo.access}`;
    } else {
      axiosInstance.defaults.headers.common['Authorization'] = "";
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  methods: {
  },
  computed:{
    cartTotalLength(){
      let totalLength = 0

      for(let i=0;i<this.cart.items.length;i++){
        totalLength+=this.cart.items[i].quantity
      }

      return totalLength
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>