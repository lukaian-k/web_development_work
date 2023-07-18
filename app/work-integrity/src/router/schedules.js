import Schedules from '../views/Schedules/Schedules.vue'
import Register from '../views/Schedules/Register.vue'
import View from '../views/Schedules/View.vue'

export default [
    {
        path: '/schedules',
        name: 'Schedules',
        component: Schedules
    },
    {
        path: '/schedules/register',
        name: 'Register Schedules',
        component: Register
    },
    {
        path: '/schedules/view',
        name: 'View Schedules',
        component: View
    },
]