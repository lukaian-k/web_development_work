import { createStore } from 'vuex'

const store = createStore({
    state: {
        isAuthenticated: false,
        user: null,
    },
    mutations: {
        SET_AUTHENTICATED(state, isAuthenticated) {
            state.isAuthenticated = isAuthenticated
            localStorage.setItem('isAuthenticated', isAuthenticated)
        },
        SET_USER(state, user) {
            state.user = user
            localStorage.setItem('user', JSON.stringify(user))
        },
    },
    actions: {
        login({ commit }, user) {
            commit('SET_AUTHENTICATED', true)
            commit('SET_USER', user)
        },
        logout({ commit }) {
            localStorage.removeItem('isAuthenticated')
            localStorage.removeItem('user')
            commit('SET_AUTHENTICATED', false)
            commit('SET_USER', null)
        },
    },
})

const isAuthenticated = localStorage.getItem('isAuthenticated')
const user = JSON.parse(localStorage.getItem('user'))

if (isAuthenticated) {
    store.commit('SET_AUTHENTICATED', isAuthenticated === 'true')
}

if (user) {
    store.commit('SET_USER', user)
}

export default store