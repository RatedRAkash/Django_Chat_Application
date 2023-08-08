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
      <div class="navbar-end">
        <router-link to="/summer" class="navbar-item">Summer</router-link>
        <router-link to="/winter" class="navbar-item">Winter</router-link>

        <div class="navbar-item">
          <div class="buttons">
            <router-link to="/log-in" class="button is-light">Log In</router-link>

            <router-link to="/cart" class="button is-success">
              <span class="icon"><i class="fas fa-shopping-cart"></i></span>
              <span>Cart</span>
            </router-link>
          </div>
        </div>
      </div>

    </div>
  </nav>

    <section class="section">
      <!-- `router-view` TAG ta jei Route ee gese shei Route er COMPONENT ke automatic Import korte pare -->
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (Akash) 2023</p>
    </footer>

  </div>

</template>

<script>

export default {
  name: 'App',
  components: {
  },
  data(){
    return {
      showMobileMenu: false,
    }
  },
  methods: {

  },
}
</script>

<style lang="scss">
@import "../node_modules/bulma";
</style>