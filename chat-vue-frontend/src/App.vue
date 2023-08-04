<template>
  <nav>
    <router-link to="/">Home</router-link> |    <!-- Normal `href` Tag use nah kore...`router-link` TAG ta use korle VUE shei Request ke intercept kore and nijei shei route ee niye jabe without Network Call to SERVER -->
    <router-link :to="{ name:'about' }">About</router-link> |
    <router-link to="/jobs">Jobs</router-link> |
    <router-link to="/chat">Chat</router-link>
  </nav>

  <button @click="redirect_to">Redirect</button>
  <button @click="go_back">Go Back</button>
  <button @click="go_forward">Go Forward</button>


  <!-- `router-view` TAG ta jei Route ee gese shei Route er COMPONENT ke automatic Import korte pare -->
  <router-view></router-view>

</template>

<script>

export default {
  name: 'App',
  components: {
  },
  methods: {
    redirect_to(){
      this.$router.push({name:'home'})
    },
    go_back(){
      this.$router.go(-1)
    },
    go_forward(){
      this.$router.go(+1)
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  padding: 10px;
  border-radius: 4px;
}

nav a.router-link-exact-active {
  color: crimson;
  background: #42b983;
}

button {
  margin: 0 10px;
  padding: 10px;
  border: none;
  border-radius: 4px;
}
</style>