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
    classrooms: []
})

axios.get('http://localhost:8000/salas/').then(res => {
    state.classrooms = res.data.map((i) => i.nome)
})
    .catch(error => {
        console.error(error)
    })

let blocks = data.Blocos
let schedules = data.Horarios
let dayWeek = data.Semana

let form = reactive({
    "nome": '',
    "sala": null,
    "bloco": null,
    "data": null,
    "hora": null
})

function onSubmit() {
    axios.post('http://localhost:8000/horarios/create/', form)
        .then(res => {
            form.nome = ''
            form.sala = ''
            form.bloco = null
            form.data = null
            form.hora = null
            isShow.value = true
        })
        .catch(error => {
            console.error(error)
        })
}
</script>

<template>
    <Title hType="h1" text="Cadastro Horários" />

    <v-sheet width="800" class="mx-auto">
        <v-container fluid>
            <v-form fast-fail @submit.prevent=onSubmit>
                <v-text-field v-model="form.nome" required label="Nome" variant="outlined" />

                <v-container fluid>
                    <v-row class="container">
                        <v-select :items="state.classrooms" required v-model="form.sala" label="Sala"></v-select>
                        <v-select :items="blocks" required class="element" v-model="form.bloco" label="Bloco"></v-select>
                    </v-row>
                    <v-row class="container">
                        <v-select :items="dayWeek" required v-model="form.data" label="Data"></v-select>
                        <v-select :items="schedules" required class="element" v-model="form.hora" label="hora"></v-select>
                    </v-row>
                </v-container>

                <br>

                <v-btn block color=var(--highlights) type="submit" variant="elevated" rounded="xl" size="large">
                    <p id="text-send">Cadastrar</p>
                </v-btn>
            </v-form>
        </v-container>
    </v-sheet>

    <SuccessAlert :isShow="isShow.valueOf()" msg="Horário cadastrado!" />
</template>

<style scoped lang="scss">
.container {
    display: flex;

    .element {
        margin-left: 10px;
    }
}

#text-send {
    color: var(--background);
}
</style>