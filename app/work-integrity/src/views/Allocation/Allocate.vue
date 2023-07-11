<script setup>
import Title from '../../components/Title.vue'
import res from './test.json'


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
                    <v-select :items="professors" label="Professor" outlined></v-select>
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
                    <label for="birthday">Data: </label>
                    <input type="date" id="birthday" name="birthday">
                </v-col>
                <v-col cols="12" md="6">
                    <label for="time">Hora: </label>
                    <input type="time" id="time" name="time">
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