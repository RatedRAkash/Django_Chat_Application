import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

import HomeView from '../views/HomeView.vue'

import SingleChatRoom from '../views/chats/SingleChatRoom.vue'
import AllRoomsView from '../views/chats/AllRoomsView.vue'

import ProductView from '../views/products/ProductView.vue'
import CategoryView from '../views/products/CategoryView.vue'
import SearchView from '../views/products/SearchView.vue'
import CartView from '../views/products/CartView.vue'

import LoginView from "../views/logins/LoginView.vue";
import RegisterView from "../views/logins/RegisterView.vue";
import LogoutView from "../views/logins/LogoutView.vue";

import NotFoundView from '../views/NotFoundView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
    // component: () => import(/* webpackChunkName: "home" */ '../views/HomeView.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'Logout',
    component: LogoutView,
    // cause without Login you can not go to LOGOUT route
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/signup',
    name: 'Register',
    component: RegisterView
  },

  {
    path: '/rooms',
    name: 'Room',
    components: {
      default: AllRoomsView,
    },
    props: true,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/rooms/:room_slug',
    name: 'chat_room',
    components: {
      default: SingleChatRoom,
    },
    props: true,
    meta: {
      requireLogin: true
    }
  },

  //single Product View Route
  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: ProductView,
    props: true
  },

  //single Category View Route
  {
    path: '/:category_slug',
    name: 'Category',
    component: CategoryView,
    props: true
  },

  //single Category View Route
  {
    path: '/search',
    name: 'Search',
    component: SearchView,
    props: true
  },

  //single Category View Route
  {
    path: '/cart',
    name: 'Cart',
    component: CartView,
    props: true
  },

  // catchAll 404 Routes
  {
    path: '/:catchAll(.*)',
    name: 'NotFound',
    component: NotFoundView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) =>{

  //*** jei sokol URL ee Meta "requireLogin" define kora ase tader ke LOGIN Route ee niya jabo jodi LOGGED IN nah takhe ***
  if(to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated){
    next({name: 'Login', query:{to: to.path}});
  }else{
    next()
  }
})

export default router