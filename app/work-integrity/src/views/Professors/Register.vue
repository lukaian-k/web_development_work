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
    "departamento": '',
    "codigo": null,
    "formacao": null
})

function onSubmit() {
    axios.post('http://localhost:8000/professores/create/', form)
        .then(res => {
            form.nome = ''
            form.departamento = ''
            form.codigo = null
            form.formacao = null
            isShow.value = true
        })
        .catch(error => {
            console.error(error)
        })
}
</script>

<template>
    <Title hType="h1" text="Cadastro Professores" />

    <v-sheet width="800" class="mx-auto">
        <v-container fluid>
            <v-form fast-fail @submit.prevent=onSubmit>
                <v-text-field v-model="form.nome" required label="Nome" variant="outlined" />
                <v-text-field v-model="form.departamento" required label="Departamento" variant="outlined" />

                <v-container fluid>
                    <v-row class="container">
                        <v-text-field v-model="form.codigo" required type="number" label="Código" variant="outlined" />
                        <v-text-field v-model="form.formacao" class="element" required label="Formação"
                            variant="outlined" />
                    </v-row>
                </v-container>

                <br>

                <v-btn block color=var(--highlights) type="submit" variant="elevated" rounded="xl" size="large">
                    <p id="text-send">Cadastrar</p>
                </v-btn>
            </v-form>
        </v-container>
    </v-sheet>

    <SuccessAlert :isShow="isShow.valueOf()" msg="Professor cadastrado!" />
</template>

<style scoped lang="scss">
.container {
    display: flex;

    .element {
        margin-left: 10px;
        width: 60%;
    }
}

#text-send {
    color: var(--background);
}
</style>