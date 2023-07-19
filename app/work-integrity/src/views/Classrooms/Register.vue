<script setup>
import Title from '../../components/Title.vue'
import SuccessAlert from '../../components/SuccessAlert.vue'
import { ref, reactive } from 'vue'
import axios from 'axios'

import { useStore } from 'vuex'
import router from "../../router"

const store = useStore()

if (!store.state.isAuthenticated) {
    router.push('/sign-in')
}

let isShow = ref(false)

let form = reactive({
    "nome": '',
    "capacidade": null,
    "bloco": ''
})

function onSubmit() {
    axios.post('http://localhost:8000/salas/create/', form)
        .then(res => {
            form.nome = ''
            form.capacidade = null
            form.bloco = ''
            isShow.value = true
        })
        .catch(error => {
            console.error(error)
        })
}
</script>

<template>
    <Title hType="h1" text="Cadastro de Salas de Aula" />

    <v-sheet width="800" class="mx-auto">
        <v-container fluid>
            <v-form fast-fail @submit.prevent=onSubmit>
                <v-text-field v-model="form.nome" required label="Nome da Sala" />
                <v-text-field v-model="form.capacidade" required type="number" label="Capacidade" />
                <v-text-field v-model="form.bloco" required label="Bloco" />

                <br>

                <v-btn block color=var(--highlights) type="submit" variant="elevated" rounded="xl" size="large">
                    <p id="text-send">Cadastrar</p>
                </v-btn>
            </v-form>
        </v-container>
    </v-sheet>

    <SuccessAlert :isShow="isShow.valueOf()" msg="Sala cadastrado!" />
</template>

<style scoped>
#text-send {
    color: var(--background);
}
</style>