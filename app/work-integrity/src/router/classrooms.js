import Classrooms from '../views/Classrooms/Classrooms.vue'
import Register from '../views/Classrooms/Register.vue'

export default [
    {
        path: '/classrooms',
        name: 'Classrooms',
        component: Classrooms
    },
    {
        path: '/classrooms/register',
        name: 'Register Classrooms',
        component: () => Register
    },
]