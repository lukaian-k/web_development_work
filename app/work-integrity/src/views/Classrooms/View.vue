<script setup>
import Title from '../../components/Title.vue'
import Card from '../../components/CardViewClassrooms.vue'
import { ref, reactive, computed } from 'vue'
import axios from 'axios'

import { useStore } from 'vuex'
import router from "../../router"

const store = useStore()

if (!store.state.isAuthenticated) {
    router.push('/sign-in')
}

const state = reactive({
    classrooms: null
})

let filtro = ref('')

axios.get('http://localhost:8000/salas/').then(res => {
    state.classrooms = res.data
})
    .catch(error => {
        console.error(error)
    })

const listaFiltrada = computed(() => {
    const nomesFiltrados = filtro.value.toLowerCase().trim()

    if (!nomesFiltrados) {
        return state.classrooms
    }

    return state.classrooms
        .filter(classroom => classroom.nome.toLowerCase().includes(nomesFiltrados))
})
</script>

<template>
    <Title hType="h1" text="Salas de Aula" />

    <br>

    <input v-model="filtro" type="text" placeholder="Digite o nome da sala">

    <div v-for="i in listaFiltrada" :key="i.nome">
        <Card :sala="i"></Card>
    </div>
</template>

<style scoped lang="scss">
input {
    margin-bottom: 2em;
    padding: 1em;
    background-color: var(--background-gray);
    border-radius: 3px;
    border: 1px solid #020202;
}
</style>