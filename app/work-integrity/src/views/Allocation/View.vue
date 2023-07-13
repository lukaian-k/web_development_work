<script setup>
import Title from '../../components/Title.vue'
import Card from '../../components/CardViewAllocation.vue'
import { ref, reactive, computed } from 'vue'
import axios from 'axios'

const state = reactive({
    allocations: null
})

let filtro = ref('')

axios.get('http://localhost:8000/alocacoes/').then(res => {
    state.allocations = res.data
})
    .catch(error => {
        console.error(error)
    })

axios.get('http://localhost:8000/professores/').then(res => {
    state.allocations.map((i) => {
        i.professor = res.data[i.professor - 1].nome
    })
})
    .catch(error => {
        console.error(error)
    })

const listaFiltrada = computed(() => {
    const nomesFiltrados = filtro.value.toLowerCase().trim()

    if (!nomesFiltrados) {
        return state.allocations
    }

    return state.allocations
        .filter(allocation => allocation.professor.toLowerCase().includes(nomesFiltrados))
})
</script>

<template>
    <v-container>
        <Title hType="h1" text="Visualizar Alocações" />

        <br>

        <input v-model="filtro" type="text" placeholder="Digite o nome do professor">

        <div v-for="allocation in listaFiltrada" :key="allocation.professor">
            <Card :allocation="allocation"></Card>
        </div>
    </v-container>
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