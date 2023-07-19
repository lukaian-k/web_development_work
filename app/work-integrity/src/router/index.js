import { createRouter, createWebHistory } from 'vue-router'

import FullLayout from '../layouts/Full.vue'
import BlankLayout from '../layouts/Blank.vue'

import Home from '../views/Home.vue'
import Professors from './professors'
import Classrooms from './classrooms'
import Allocation from './allocation'
import Schedules from './schedules'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: BlankLayout,
      children: [
        {
          path: '',
          name: 'Welcome',
          component: () => import('../views/Welcome.vue')
        },
        {
          path: '/sign-in',
          name: 'Sign-in',
          component: () => import('../views/Login.vue')
        },
        {
          path: '/development-page',
          name: 'Development Page',
          component: () => import('../views/DevelopmentPage.vue')
        }
      ]
    },
    {
      path: '/',
      component: FullLayout,
      children: [
        {
          path: '/home',
          name: 'Home',
          component: Home
        },
        ...Professors,
        ...Classrooms,
        ...Allocation,
        ...Schedules,
        {
          path: '/courses',
          name: 'Courses',
          component: () => import('../views/Courses/Courses.vue')
        }
      ]
    }
  ]
})

export default router