<script setup>
import Title from '../../components/Title.vue'
import data from './data.json'
import { reactive } from 'vue'
import axios from 'axios'

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
let time = data.Horarios

function submitForm() {
    console.log('Formulário enviado!')
}
</script>  

<template>
    <v-container>
        <Title hType="h1" text="Alocar Professores" />

        <br>

        <v-form>
            <v-row>
                <v-col cols="12" md="6">
                    <v-select :items="state.professors" label="Professor" outlined></v-select>
                </v-col>
                <v-col cols="12" md="6">
                    <v-select :items="courses" label="Curso" outlined></v-select>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" md="6">
                    <v-select :items="rooms" label="Sala" outlined></v-select>
                </v-col>
                <v-col cols="12" md="6">
                    <v-select :items="blocks" label="Bloco" outlined></v-select>
                </v-col>
            </v-row>

            <v-row>
                <v-col cols="12" md="6">
                    <v-select :items="time" label="Horário" outlined></v-select>
                </v-col>
            </v-row>

            <br>

            <v-btn class="btn" @click="submitForm">Alocar</v-btn>
        </v-form>
    </v-container>
</template>

<style scoped lang="scss">
$background: var(--background);
$highlights: var(--highlights);

.btn {
    color: $background;
    background-color: $highlights;
}
</style>