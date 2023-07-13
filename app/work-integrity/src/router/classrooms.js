import Classrooms from '../views/Classrooms/Classrooms.vue'
import Register from '../views/Classrooms/Register.vue'
import View from '../views/Classrooms/View.vue'

export default [
    {
        path: '/classrooms',
        name: 'Classrooms',
        component: Classrooms
    },
    {
        path: '/classrooms/register',
        name: 'Register Classrooms',
        component: Register
    },
    {
        path: '/classrooms/view',
        name: 'View Classrooms',
        component: View
    },
]