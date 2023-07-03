<script setup>
import Title from '../../components/Title.vue';
import { RouterLink } from 'vue-router'
</script>

<template>
    <v-app>
        <v-container>
            <Title hType="h1" text="Sala de Aula" />
            <v-row class="options">
                <v-col cols="12" sm="6" md="4">
                    <RouterLink to="/classrooms/register">
                        <v-card class="option-card">
                            <v-card-title>Cadastrar Sala de Aula</v-card-title>
                        </v-card>
                    </RouterLink>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                    <RouterLink to="/development-page">
                        <v-card class="option-card">
                            <v-card-title>Visualizar Salas de Aula</v-card-title>
                        </v-card>
                    </RouterLink>
                </v-col>
            </v-row>
        </v-container>
    </v-app>
</template>

<style scoped lang="scss">
$background: var(--background);
$background-gray: var(--background-gray);

.options {
    margin-top: 3rem;
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