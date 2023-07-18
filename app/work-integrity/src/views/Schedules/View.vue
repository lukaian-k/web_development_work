<script setup>
import Title from '../../components/Title.vue'
import Card from '../../components/CardViewProfessors.vue'
import { ref, reactive, computed } from 'vue'
import axios from 'axios'

const state = reactive({
    professores: null
})

let filtro = ref('')

axios.get('http://localhost:8000/professores/').then(res => {
    state.professores = res.data
})
    .catch(error => {
        console.error(error)
    })

const listaFiltrada = computed(() => {
    const nomesFiltrados = filtro.value.toLowerCase().trim()

    if (!nomesFiltrados) {
        return state.professores
    }

    return state.professores
        .filter(professor => professor.nome.toLowerCase().includes(nomesFiltrados))
})
</script>

<template>
    <Title hType="h2" text="Professores UFC - Campus Russas" />

    <br>

    <input v-model="filtro" type="text" placeholder="Digite o nome do professor">

    <div v-for="i in listaFiltrada" :key="i.nome">
        <Card :professor="i"></Card>
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