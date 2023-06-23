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
          path: '/courses',
          name: 'Courses',
          component: () => import('../views/Courses.vue')
        }
      ]
    },
    {
      path: '/',
      component: () => import('../layouts/Blank.vue'),
      children: [
        {
          path: '/sign-in',
          name: 'Sign-in',
          component: () => import('../views/Login.vue')
        }
      ]
    }
  ]
})

export default router
