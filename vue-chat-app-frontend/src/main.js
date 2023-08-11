import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueRouter from 'vue-router';
import store from './store';   // Import your Vuex store configuration

// import 'bootstrap/dist/css/bootstrap.min.css';
// import 'bootstrap';
import $ from 'jquery';

// CUSTOM axiosInstance
import axiosInstance from "@/axios";

// axiosInstance.defaults.baseURL = 'http://localhost:7070'

const app = createApp(App)
// Use the router and store & MUST .use before MOUTING to (#app)
app.use(router);
app.use(store);

// Mount the app
app.mount('#app');