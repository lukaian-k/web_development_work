import Allocation from '../views/Allocation/Allocation.vue'
import Allocate from '../views/Allocation/Allocate.vue'
import View from '../views/Allocation/View.vue'

export default [
    {
        path: '/allocation',
        name: 'Allocation',
        component: Allocation
    },
    {
        path: '/allocation/allocate',
        name: 'Allocate Professors',
        component: Allocate
    },
    {
        path: '/allocation/view',
        name: 'View Allocation',
        component: View
    },
]