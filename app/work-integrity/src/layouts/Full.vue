<script>
import { RouterLink, RouterView } from 'vue-router'

import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'

export default {
    name: 'Full',
    components: {
        Header,
        Footer
    }
}
</script>

<template>
    <v-app>
        <Header />

        <v-main>
            <v-container>
                <RouterView />
            </v-container>
        </v-main>

        <Footer />
    </v-app>
</template>

<style></style>