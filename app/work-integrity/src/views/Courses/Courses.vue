<script setup>
import Title from '../../components/Title.vue'
import Card from '../../components/CardViewCurso.vue'
import data from './data.json'

</script>

<template>
    <v-app>
        <v-container>
            <Title hType="h1" text="Cursos e Disciplinas" />

            <br>

            <v-row class="cursos">
                <p v-for="i in data.Cursos">| {{ i }} |</p>
            </v-row>
            <Card :list="data.Disciplinas" />
        </v-container>
    </v-app>
</template>

<style scoped lang="scss">
.cursos {
    display: flex;
    justify-content: center;
    margin: 10px 0px;
}
</style>