import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import JobsView from '../views/jobs/JobsView.vue'
import JobDetaisView from '../views/jobs/JobDetailsView.vue'
import ChatRoomView from '../views/chats/ChatRoom.vue'
import ProductView from '../views/products/ProductView.vue'

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
    path: '/chat',
    name: 'chat_room',
    components: {
      default: ChatRoomView,
    },
    props: true
  },

  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: ProductView,
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