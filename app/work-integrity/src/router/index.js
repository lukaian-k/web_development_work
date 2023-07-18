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
      component: FullLayout,
      children: [
        {
          path: '',
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
    },
    {
      path: '/',
      component: BlankLayout,
      children: [
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
    }
  ]
})

export default router