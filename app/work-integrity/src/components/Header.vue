<script>
import { RouterLink } from 'vue-router'
</script>

<template>
    <v-app-bar app color=var(--highlights)>
        <v-app-bar-icon>
            <RouterLink to="/home">
                <img id="icon-ufc" src="../assets/icon-ufc-header.svg" alt="icone da UFC">
            </RouterLink>
        </v-app-bar-icon>

        <template v-slot:append>
            <RouterLink to="/development-page">Logout</RouterLink>
        </template>

    </v-app-bar>
</template>

<style scoped>
#icon-ufc {
    margin-left: 2em;
}
</style>