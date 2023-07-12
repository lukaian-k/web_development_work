<script setup>
import Title from '../../components/Title.vue'
import Card from '../../components/CardViewProfessors.vue'
import { reactive } from 'vue'
import axios from 'axios'

const state = reactive({
    professores: null
})

axios.get('http://localhost:8000/professores/').then(res => {
    state.professores = res.data
})
    .catch(error => {
        console.error(error)
    })
</script>

<template>
    <Title hType="h2" text="Professores UFC - Campus Russas" />

    <br>

    <div v-for="i in state.professores" :key="i.nome">
        <Card :professor="i"></Card>
    </div>
</template>