<script setup>
import Title from '../../components/Title.vue'
import Menu from '../../components/Menu.vue'

let items = [
    {
        title: "Cadastrar Professores",
        router: "/professors/register"
    },
    {
        title: "Visualizar Professores",
        router: "/professors/view"
    }
]
</script>

<template>
    <v-app>
        <v-container>
            <Title hType="h1" text="Professores" />
            <Menu :items="items" />
        </v-container>
    </v-app>
</template>