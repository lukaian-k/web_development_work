import { createStore } from 'vuex'

const store = createStore({
    state: {
        isAuthenticated: false,
        user: null,
    },
    mutations: {
        SET_AUTHENTICATED(state, isAuthenticated) {
            state.isAuthenticated = isAuthenticated
        },
        SET_USER(state, user) {
            state.user = user
        },
    },
    actions: {
        login({ commit }, user) {
            // Lógica: login

            commit('SET_AUTHENTICATED', true)
            commit('SET_USER', user)
        },
        logout({ commit }) {
            // Lógica: logout

            commit('SET_AUTHENTICATED', false)
            commit('SET_USER', null)
        },
    },
})

export default store