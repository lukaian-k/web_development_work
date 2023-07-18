<script setup>
import Title from '../../components/Title.vue'
import Menu from '../../components/Menu.vue'

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