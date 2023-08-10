import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'

import JobsView from '../views/jobs/JobsView.vue'
import JobDetaisView from '../views/jobs/JobDetailsView.vue'

import ChatRoom from '../views/chats/ChatRoom.vue'
import RoomView from '../views/chats/RoomView.vue'

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
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
    // component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'Logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'Register',
    component: RegisterView
  },

  {
    path: '/jobs',
    name: 'jobs',
    component: JobsView
  },
  {
    path: '/jobs/:id',
    name: 'job_details',
    component: JobDetaisView,
    props: true
  },

  // redirect
  {
    path: '/all-jobs',
    redirect: '/jobs',
  },

  {
    path: '/rooms',
    name: 'Room',
    components: {
      default: RoomView,
    },
    props: true
  },
  {
    path: '/rooms/:room_slug',
    name: 'chat_room',
    components: {
      default: ChatRoom,
    },
    props: true
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

export default router