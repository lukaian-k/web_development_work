<script setup>
import Title from '../../components/Title.vue'
import Card from '../../components/CardViewAllocation.vue';

let allocations = [
    { id: 1, course: 'Curso 1', professor: 'Professor 1', room: 'Sala 1', block: 'Bloco 1' },
    { id: 2, course: 'Curso 2', professor: 'Professor 2', room: 'Sala 2', block: 'Bloco 2' },
    { id: 3, course: 'Curso 3', professor: 'Professor 3', room: 'Sala 3', block: 'Bloco 3' },
]
</script>

<template>
    <v-container>
        <Title hType="h1" text="Visualizar Alocações" />

        <br>

        <div v-for="allocation in allocations" :key="allocation.id">
            <Card :allocation="allocation"></Card>
        </div>
    </v-container>
</template>
  