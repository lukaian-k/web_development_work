import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: () => import('../layouts/Full.vue'),
      children: [
        {
          path: '',
          name: 'Home',
          component: Home
        },
        {
          path: '/sign-in',
          name: 'Cadastrar',
          component: () => import('../views/Cadastrar.vue')
        }
      ]
    },
    {
      path: '/',
      component: () => import('../layouts/Blank.vue'),
      children: [
        {
          path: '/login',
          name: 'Login',
          component: () => import('../views/Login.vue')
        }
      ]
    }
  ]
})

export default router
