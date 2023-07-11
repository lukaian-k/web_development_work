<script setup>
defineProps({
    professor: {
        type: Object,
        required: true,
    }
})
</script>

<template>
    <v-card class="professor-card">
        <v-row no-gutters align="center">
            <v-card-text>
                <h3>{{ professor.nome }}</h3>
                <p>Departamento: {{ professor.dep }}</p>
                <p>Código: {{ professor.cod }}</p>
                <p>Formação: {{ professor.formacao }}</p>
            </v-card-text>
        </v-row>
    </v-card>
</template>

<style scoped lang="scss">
.professor-card {
    margin-bottom: 20px;

    h3 {
        margin-top: 0;
    }

    p {
        margin: 0;
    }
}
</style>