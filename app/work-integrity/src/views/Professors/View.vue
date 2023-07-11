<script setup>
import Title from '../../components/Title.vue'
import Card from '../../components/CardViewProfessors.vue'
import res from './test.json'
</script>

<template>
    <Title hType="h2" text="Professores UFC - Campus Russas" />

    <br>

    <div v-for="i in res.Professores" :key="i.nome">
        <Card :professor="i"></Card>
    </div>
</template>