<script setup>
import Title from '../../components/Title.vue';
import { RouterLink } from 'vue-router'
</script>

<template>
    <v-app>
        <v-container>
            <Title hType="h1" text="Professores" />
            <div class="options">
                <v-col cols="12" sm="6" md="4">
                    <RouterLink to="/professors/register">
                        <v-card class="option-card">
                            <v-card-title>Cadastrar Professores</v-card-title>
                        </v-card>
                    </RouterLink>
                </v-col>
                <v-col cols="12" sm="6" md="4">
                    <RouterLink to="/professors/view">
                        <v-card class="option-card">
                            <v-card-title>Visualizar Professores</v-card-title>
                        </v-card>
                    </RouterLink>
                </v-col>
            </div>
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