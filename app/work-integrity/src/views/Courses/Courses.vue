<script setup>
import Title from '../../components/Title.vue'
import Card from '../../components/CardViewCurso.vue'
import data from './data.json'
import { ref, computed } from 'vue'

let filtro = ref('')

const listaFiltrada = computed(() => {
    const nomesFiltrados = filtro.value.toLowerCase().trim()

    if (!nomesFiltrados) {
        return data.Disciplinas
    }

    return data.Disciplinas
        .filter(i => i.toLowerCase().includes(nomesFiltrados))
})
</script>

<template>
    <v-app>
        <v-container>
            <Title hType="h1" text="Cursos e Disciplinas" />

            <br>

            <v-row class="cursos">
                <p v-for="i in data.Cursos">| {{ i }} |</p>
            </v-row>

            <input v-model="filtro" type="text" placeholder="Digite o nome do professor">

            <Card :list="listaFiltrada" />
        </v-container>
    </v-app>
</template>

<style scoped lang="scss">
.cursos {
    display: flex;
    justify-content: center;
    margin: 10px 0px;
}

input {
    margin-bottom: 2em;
    padding: 1em;
    background-color: var(--background-gray);
    border-radius: 3px;
    border: 1px solid #020202;
}
</style>