<script setup>
import { reactive } from 'vue'
import axios from 'axios'

defineProps({
    allocation: {
        type: Object,
        required: true,
    }
})

const state = reactive({
    allocations: null
})

axios.get('http://localhost:8000/alocacoes/').then(res => {
    state.allocations = res.data
})
    .catch(error => {
        console.error(error)
    })

function editAllocation(id) {
    console.log('Editar alocação:', allocation)
}

function deleteAllocation(id) {
    axios.delete(`http://localhost:8000/alocacoes/${id}/excluir/`)
        .then(res => {
            console.log('Exclusão realizada com sucesso')
            alert('Exclusão realizada com sucesso')
        })
        .catch(error => {
            console.error('Ocorreu um erro ao excluir a alocação:', error)
        })
}
</script>

<template>
    <v-card class="allocation-card" outlined>
        <v-card-title>{{ allocation.curso }}</v-card-title>
        <v-card-subtitle>{{ allocation.professor }}</v-card-subtitle>
        <v-card-text>
            Sala: {{ allocation.sala }} | Bloco: {{ allocation.bloco }}
        </v-card-text>
        <v-card-text>
            Horario: {{ allocation.horario }} | Dia da Semana: {{ allocation.semana }}
        </v-card-text>
        <v-card-actions>
            <v-btn color="var(--success-indicators)" text @click="editAllocation(allocation.id)">Editar</v-btn>
            <v-btn color="error" text @click="deleteAllocation(allocation.id)">Excluir</v-btn>
        </v-card-actions>
    </v-card>
</template>

<style scoped lang="scss">
$background: var(--background);
$highlights: var(--highlights);

.allocation-card {
    margin-bottom: 20px;
    background-color: $highlights;
    color: $background;
}
</style>
