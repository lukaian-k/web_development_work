<script>
import { RouterLink, RouterView } from 'vue-router'

export default {}
</script>

<template>
    <v-app>
        <v-app-bar app>
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/sign-in">Cadastrar</RouterLink>
        </v-app-bar>

        <v-main>
            <v-container>
                <RouterView />
            </v-container>
        </v-main>
    </v-app>
</template>

<style></style>