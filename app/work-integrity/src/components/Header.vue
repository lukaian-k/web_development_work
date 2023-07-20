<script setup>
import { RouterLink } from 'vue-router'
import { useStore } from 'vuex'
import router from "../router"

const store = useStore()

function logout() {
    localStorage.removeItem('isAuthenticated')
    localStorage.removeItem('user')
    store.commit('SET_AUTHENTICATED', false)
    store.commit('SET_USER', null)

    router.push('/')
}
</script>

<template>
    <v-app-bar app color=var(--highlights)>
        <v-app-bar-icon>
            <RouterLink to="/home">
                <img id="icon-ufc" src="../assets/icon-ufc-header.svg" alt="icone da UFC">
            </RouterLink>
        </v-app-bar-icon>

        <template v-slot:append>
            <v-btn class="btn" @click="logout">Logout</v-btn>
        </template>
    </v-app-bar>
</template>

<style scoped>
#icon-ufc {
    margin-left: 2em;
}

.btn {
    color: var(--background);
}
</style>