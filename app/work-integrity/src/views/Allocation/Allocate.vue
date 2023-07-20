<script setup>
import Title from '../../components/Title.vue'
import SuccessAlert from '../../components/SuccessAlert.vue'
import data from './data.json'
import { ref, reactive } from 'vue'
import axios from 'axios'

import { useStore } from 'vuex'
import router from "../../router"

const store = useStore()

if (!store.state.isAuthenticated) {
    router.push('/sign-in')
}

let isShow = ref(false)

const state = reactive({
    professors: [],
    classrooms: [],
    courses: []
})

axios.get('http://localhost:8000/professores/').then(res => {
    state.professors = res.data.map((i) => i.nome)
})
    .catch(error => {
        console.error(error)
    })

axios.get('http://localhost:8000/salas/').then(res => {
    state.classrooms = res.data.map((i) => i.nome)
})
    .catch(error => {
        console.error(error)
    })

axios.get('http://localhost:8000/curso/').then(res => {
    state.courses = res.data.map((i) => i.nome)
})
    .catch(error => {
        console.error(error)
    })

let blocks = data.Blocos
let schedules = data.Horarios
let dayWeek = data.Semana

let form = reactive({
    "professor": null,
    "curso": null,
    "horario": '',
    "sala": null,
    "bloco": '',
    "semana": ''
})

function submitForm() {
    state.professors.forEach((i, index) => {
        if (form.professor == i) {
            form.professor = index + 1
        }
    })

    state.classrooms.forEach((i, index) => {
        if (i == state.classrooms[index]) {
            form.sala = index + 1
        }
    })

    state.courses.forEach((i, index) => {
        if (i == state.courses[index]) {
            form.curso = index + 1
        }
    })

    axios.post('http://localhost:8000/alocacoes/create/', form)
        .then(res => {
            form.professor = null
            form.curso = null
            form.horario = ''
            form.sala = null
            form.bloco = ''
            form.semana = ''
            isShow.value = true
        })
        .catch(error => {
            console.error(error)
        })
}
</script>

<template>
    <v-container>
        <Title hType="h1" text="Alocar Professores" />

        <br>

        <v-form>
            <v-row>
                <v-col cols="12" md="6">
                    <v-select v-model="form.professor" :items="state.professors" label="Professor" outlined></v-select>
                </v-col>
                <v-col cols="12" md="6">
                    <v-select v-model="form.curso" :items="state.courses" label="Curso" outlined></v-select>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" md="6">
                    <v-select v-model="form.sala" :items="state.classrooms" label="Sala" outlined></v-select>
                </v-col>
                <v-col cols="12" md="6">
                    <v-select v-model="form.bloco" :items="blocks" label="Bloco" outlined></v-select>
                </v-col>
            </v-row>

            <v-row>
                <v-col cols="12" md="6">
                    <v-select v-model="form.horario" :items="schedules" label="Horário" outlined></v-select>
                </v-col>
                <v-col cols="12" md="6">
                    <v-select v-model="form.semana" :items="dayWeek" label="Dia da Semana" outlined></v-select>
                </v-col>
            </v-row>

            <br>

            <v-btn class="btn" @click="submitForm">Alocar</v-btn>
        </v-form>
    </v-container>

    <SuccessAlert :isShow="isShow.valueOf()" msg="Alocação feita!" />
</template>

<style scoped lang="scss">
$background: var(--background);
$highlights: var(--highlights);

.btn {
    color: $background;
    background-color: $highlights;
}
</style>