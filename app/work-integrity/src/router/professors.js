import Professors from '../views/Professors/Professors.vue'
import Register from '../views/Professors/Register.vue'
import View from '../views/Professors/View.vue'

export default [
    {
        path: '/professors',
        name: 'Professors',
        component: Professors
    },
    {
        path: '/professors/register',
        name: 'Register Professors',
        component: Register
    },
    {
        path: '/professors/view',
        name: 'View Professors',
        component: View
    },
]