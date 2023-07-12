<script setup>
import Title from '../../components/Title.vue'
import Card from '../../components/CardViewAllocation.vue';
import { ref, computed } from 'vue'

let filtro = ref('')

let allocations = [
    { id: 1, course: 'Curso 1', professor: 'Professor 1', room: 'Sala 1', block: 'Bloco 1' },
    { id: 2, course: 'Curso 2', professor: 'Professor 2', room: 'Sala 2', block: 'Bloco 2' },
    { id: 3, course: 'Curso 3', professor: 'Professor 3', room: 'Sala 3', block: 'Bloco 3' },
]

const listaFiltrada = computed(() => {
    const nomesFiltrados = filtro.value.toLowerCase().trim()

    if (!nomesFiltrados) {
        return allocations
    }

    return allocations
        .filter(professor => professor.course.toLowerCase().includes(nomesFiltrados))
})
</script>

<template>
    <v-container>
        <Title hType="h1" text="Visualizar Alocações" />

        <br>

        <input v-model="filtro" type="text" placeholder="Digite o nome do professor">

        <div v-for="allocation in listaFiltrada" :key="allocation.id">
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