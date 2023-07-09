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
          component: () => import('../views/Courses/Courses.vue')
        },
        {
          path: '/professors',
          name: 'Professors',
          component: () => import('../views/Professors/Professors.vue')
        },
        {
          path: '/professors/register',
          name: 'Register Professors',
          component: () => import('../views/Professors/Register.vue')
        },
        {
          path: '/schedules',
          name: 'Schedules',
          component: () => import('../views/Schedules/Schedules.vue')
        },
        {
          path: '/classrooms',
          name: 'Classrooms',
          component: () => import('../views/Classrooms/Classrooms.vue')
        },
        {
          path: '/classrooms/register',
          name: 'Register Classrooms',
          component: () => import('../views/Classrooms/Register.vue')
        },
        {
          path: '/allocation',
          name: 'Allocation',
          component: () => import('../views/Allocation/Allocation.vue')
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