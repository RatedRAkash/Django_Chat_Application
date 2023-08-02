import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// MyComponent.vue
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';
import '@fortawesome/fontawesome-free/css/all.min.css';
import $ from 'jquery';


createApp(App).use(router).mount('#app')
