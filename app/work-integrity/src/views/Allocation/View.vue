<script setup>
import Title from '../../components/Title.vue'
import Card from '../../components/CardViewAllocation.vue'
import { reactive } from 'vue'
import axios from 'axios'

import { useStore } from 'vuex'
import router from "../../router"

const store = useStore()

if (!store.state.isAuthenticated) {
    router.push('/sign-in')
}

const state = reactive({
    allocations: null,
    allocationsOrder: {
        "Segunda-Feira": {
            "08:00:00": [],
            "10:00:00": [],
            "13:30:00": [],
            "15:30:00": []
        },
        "Terça-Feira": {
            "08:00:00": [],
            "10:00:00": [],
            "13:30:00": [],
            "15:30:00": []
        },
        "Quarta-Feira": {
            "08:00:00": [],
            "10:00:00": [],
            "13:30:00": [],
            "15:30:00": []
        },
        "Quinta-Feira": {
            "08:00:00": [],
            "10:00:00": [],
            "13:30:00": [],
            "15:30:00": []
        },
        "Sexta-Feira": {
            "08:00:00": [],
            "10:00:00": [],
            "13:30:00": [],
            "15:30:00": []
        }
    }
})

axios.get('http://localhost:8000/alocacoes/').then(res => {
    state.allocations = res.data

    axios.get('http://localhost:8000/professores/').then(res => {
        state.allocations.map((i) => {
            i.professor = res.data[i.professor - 1].nome
        })
    })
        .catch(error => {
            console.error(error)
        })

    axios.get('http://localhost:8000/curso/').then(res => {
        state.allocations.map((i) => {
            i.curso = res.data[i.curso - 1].nome
        })
    })
        .catch(error => {
            console.error(error)
        })

    state.allocations.forEach(i => {
        state.allocationsOrder[i.semana][i.horario].push(i)
    })
    console.log(state.allocationsOrder)
})
    .catch(error => {
        console.error(error)
    })
</script>

<template>
    <v-container>
        <Title hType="h1" text="Visualizar Alocações" />

        <br>

        <div class="grid">
            <div class="column">
                <h3>Segunda-Feira</h3>

                <br>

                <p>08:00-10:00</p>

                <div v-for="allocation in state.allocationsOrder['Segunda-Feira']['08:00:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>

                <p>10:00-12:00</p>

                <div v-for="allocation in state.allocationsOrder['Segunda-Feira']['10:00:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>

                <p>13:30-15:30</p>

                <div v-for="allocation in state.allocationsOrder['Segunda-Feira']['13:30:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>

                <p>15:30-17:30</p>

                <div v-for="allocation in state.allocationsOrder['Segunda-Feira']['15:30:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>
            </div>

            <div class="column">
                <h3>Terça-Feira</h3>

                <br>

                <p>08:00-10:00</p>

                <div v-for="allocation in state.allocationsOrder['Terça-Feira']['08:00:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>

                <p>10:00-12:00</p>

                <div v-for="allocation in state.allocationsOrder['Terça-Feira']['10:00:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>

                <p>13:30-15:30</p>

                <div v-for="allocation in state.allocationsOrder['Terça-Feira']['13:30:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>

                <p>15:30-17:30</p>

                <div v-for="allocation in state.allocationsOrder['Terça-Feira']['15:30:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>
            </div>

            <div class="column">
                <h3>Quarta-Feira</h3>

                <br>

                <p>08:00-10:00</p>

                <div v-for="allocation in state.allocationsOrder['Quarta-Feira']['08:00:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>

                <p>10:00-12:00</p>

                <div v-for="allocation in state.allocationsOrder['Quarta-Feira']['10:00:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>

                <p>13:30-15:30</p>

                <div v-for="allocation in state.allocationsOrder['Quarta-Feira']['13:30:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>

                <p>15:30-17:30</p>

                <div v-for="allocation in state.allocationsOrder['Quarta-Feira']['15:30:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>
            </div>

            <div class="column">
                <h3>Quinta-Feira</h3>

                <br>

                <p>08:00-10:00</p>

                <div v-for="allocation in state.allocationsOrder['Quinta-Feira']['08:00:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>

                <p>10:00-12:00</p>

                <div v-for="allocation in state.allocationsOrder['Quinta-Feira']['10:00:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>

                <p>13:30-15:30</p>

                <div v-for="allocation in state.allocationsOrder['Quinta-Feira']['13:30:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>

                <p>15:30-17:30</p>

                <div v-for="allocation in state.allocationsOrder['Quinta-Feira']['15:30:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>
            </div>

            <div class="column">
                <h3>Sexta-Feira</h3>

                <br>

                <p>08:00-10:00</p>

                <div v-for="allocation in state.allocationsOrder['Sexta-Feira']['08:00:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>

                <p>10:00-12:00</p>

                <div v-for="allocation in state.allocationsOrder['Sexta-Feira']['10:00:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>

                <p>13:30-15:30</p>

                <div v-for="allocation in state.allocationsOrder['Sexta-Feira']['13:30:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>

                <p>15:30-17:30</p>

                <div v-for="allocation in state.allocationsOrder['Sexta-Feira']['15:30:00']" :key="allocation.professor">
                    <Card :allocation="allocation"></Card>
                </div>
            </div>
        </div>
    </v-container>
</template>

<style scoped lang="scss">
.grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 20px;
}

p {
    font-weight: bold;
}
</style>