<script setup>
import { RouterView } from 'vue-router'

import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
</script>

<template>
    <v-app>
        <Header />

        <v-main>
            <br>
            <v-container>
                <RouterView />
            </v-container>
            <br>
        </v-main>

        <Footer />
    </v-app>
</template>

<style></style>