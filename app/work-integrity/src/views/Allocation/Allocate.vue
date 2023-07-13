<script setup>
import Title from '../../components/Title.vue'
import SuccessAlert from '../../components/SuccessAlert.vue'
import data from './data.json'
import { ref, reactive } from 'vue'
import axios from 'axios'

let isShow = ref(false)

const state = reactive({
    professors: []
})

axios.get('http://localhost:8000/professores/').then(res => {
    state.professors = res.data.map((i) => i.nome)
})
    .catch(error => {
        console.error(error)
    })

let courses = data.Cursos
let rooms = data.Salas
let blocks = data.Blocos
let schedules = data.Horarios
let dayWeek = data.Semana

let form = reactive({
    "professor": '',
    "curso": '',
    "horario": '',
    "sala": '',
    "bloco": '',
    "semana": ''
})

function submitForm() {
    axios.post('http://localhost:8000/alocacoes/create/', form)
        .then(res => {
            form.professor = ''
            form.curso = ''
            form.horario = ''
            form.sala = ''
            form.bloco = ''
            form.semana = ''
            form.isShow.value = true
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
                    <v-select v-model="form.curso" :items="courses" label="Curso" outlined></v-select>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" md="6">
                    <v-select v-model="form.sala" :items="rooms" label="Sala" outlined></v-select>
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