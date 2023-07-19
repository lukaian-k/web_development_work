<script setup>
import Title from '../../components/Title.vue'
import Menu from '../../components/Menu.vue'

import { useStore } from 'vuex'
import router from "../../router"

const store = useStore()

if (!store.state.isAuthenticated) {
    router.push('/sign-in')
}

let items = [
    {
        title: "Cadastrar Horários",
        router: "/schedules/register"
    },
    {
        title: "Visualizar Horários",
        router: "/schedules/view"
    }
]
</script>

<template>
    <v-app>
        <v-container>
            <Title hType="h1" text="Horários" />
            <Menu :items="items" />
        </v-container>
    </v-app>
</template>