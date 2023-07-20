<script setup>
import Title from '../../components/Title.vue'
import Card from '../../components/CardViewCurso.vue'
import SuccessAlert from '../../components/SuccessAlert.vue'
import data from './data.json'
import { ref, computed } from 'vue'

import { useStore } from 'vuex'
import router from "../../router"

const store = useStore()

if (!store.state.isAuthenticated) {
    router.push('/sign-in')
}

let filtro = ref('')
let textInput = ref('')
let isShow = ref(false)

const listaFiltrada = computed(() => {
    const nomesFiltrados = filtro.value.toLowerCase().trim()

    if (!nomesFiltrados) {
        return data.Disciplinas
    }

    return data.Disciplinas
        .filter(i => i.toLowerCase().includes(nomesFiltrados))
})

function insertCourse() {
    textInput.value = ''
    isShow.value = true
}
</script>

<template>
    <v-app>
        <v-container>
            <Title hType="h1" text="Cursos e Disciplinas" />

            <br>

            <v-row class="cursos">
                <h4>Cursos: |</h4>
                <p v-for="i in data.Cursos">{{ i }}<strong>|</strong></p>
            </v-row>

            <input v-model="filtro" type="text" placeholder="Digite o nome do curso">

            <Card :list="listaFiltrada" />

            <div class="floating-form">
                <v-text-field v-model="textInput" label="Nome do curso"></v-text-field>
                <v-btn class="btn" @click="insertCourse">Inserir</v-btn>
            </div>

            <SuccessAlert :isShow="isShow.valueOf()" msg="Curso adicionado!" />
        </v-container>
    </v-app>
</template>

<style scoped lang="scss">
$background: var(--background);
$background-gray: var(--background-gray);
$highlights: var(--highlights);

.cursos {
    display: flex;
    justify-content: center;
    margin: 10px 0px;
}

input {
    margin-bottom: 2em;
    padding: 1em;
    background-color: $background-gray;
    border-radius: 3px;
    border: 1px solid #020202;
}

.floating-form {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 10px 0px 10px;
    background-color: $background;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    width: 80%;
    max-width: 600px;

    .btn {
        margin-left: 10px;
        background-color: $highlights;
        color: $background;
    }
}
</style>