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
        title: "Alocar Professores",
        router: "/allocation/allocate"
    },
    {
        title: "Visualizar Alocações",
        router: "/allocation/view"
    }
]
</script>

<template>
    <v-app>
        <v-container>
            <Title hType="h1" text="Alocação" />
            <Menu :items="items" />
        </v-container>
    </v-app>
</template>

<style scoped lang="scss">
$background: var(--background);
$background-gray: var(--background-gray);

.options {
    margin-top: 2rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.option-card {
    cursor: pointer;
    text-align: center;
    padding: 2rem;
    background-color: $background;
    transition: background-color 0.3s;

    &:hover {
        background-color: $background-gray;
    }
}
</style>