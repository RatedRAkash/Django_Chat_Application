import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueRouter from 'vue-router';

// import 'bootstrap/dist/css/bootstrap.min.css';
// import 'bootstrap';
import $ from 'jquery';
import axios from "axios";

axios.defaults.baseURL = 'http://localhost:7070'
createApp(App).use(router).mount('#app')