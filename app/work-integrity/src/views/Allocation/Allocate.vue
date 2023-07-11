<script setup>
import Title from '../../components/Title.vue'
import res from './test.json'

let selectedProfessor = null
let selectedCourse = null
let selectedRoom = null
let selectedBlock = null
let selectedDate = null
let selectedTime = null
let professors = res.Professores.map((prof) => prof.nome)
let courses = res.Cursos
let rooms = res.Salas
let blocks = ['Bloco 1', 'Bloco 2']

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
                    <v-select v-model="selectedProfessor" :items="professors" label="Professor" outlined></v-select>
                </v-col>
                <v-col cols="12" md="6">
                    <v-select v-model="selectedCourse" :items="courses" label="Curso" outlined></v-select>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" md="6">
                    <v-select v-model="selectedRoom" :items="rooms" label="Sala" outlined></v-select>
                </v-col>
                <v-col cols="12" md="6">
                    <v-select v-model="selectedBlock" :items="blocks" label="Bloco" outlined></v-select>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" md="6">
                    <v-date-picker v-model="selectedDate" label="Data" outlined></v-date-picker>
                </v-col>
                <v-col cols="12" md="6">
                    <v-time-picker v-model="selectedTime" label="Hora" format="24hr" outlined></v-time-picker>
                </v-col>
            </v-row>
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