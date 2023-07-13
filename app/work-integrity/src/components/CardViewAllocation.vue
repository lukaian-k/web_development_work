<script setup>
defineProps({
    allocation: {
        type: Object,
        required: true,
    }
})

function editAllocation() {
    console.log('Editar alocação:', this.allocation)
}

function deleteAllocation() {
    console.log('Excluir alocação:', this.allocation)
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
            <v-btn color="var(--success-indicators)" text @click="editAllocation">Editar</v-btn>
            <v-btn color="error" text @click="deleteAllocation">Excluir</v-btn>
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
  