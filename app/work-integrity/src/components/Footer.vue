<script setup>
import { reactive } from 'vue'

const itens = reactive([
    { name: 'Cursos', route: '/courses' },
    { name: 'Professores', route: '/professors' },
    { name: 'Horários', route: '/schedules' },
    { name: 'Sala de Aula', route: '/classrooms' },
    { name: 'Alocação', route: '/allocation' }
])
</script>

<template>
    <v-footer color=var(--background-gray)>
        <v-row justify="center" no-gutters>
            <v-btn v-for="item in itens" :key=item.name variant="text" class="mx-2" rounded="xl">
                <RouterLink :to=item.route>
                    <v-list-item-title id="text" v-text=item.name />
                </RouterLink>
            </v-btn>
            <v-col class="text-center mt-4" cols="12">
                © {{ new Date().getFullYear() }} — <strong>UFC Academic Manager.</strong> Todos os direitos reservados.
            </v-col>
        </v-row>
    </v-footer>
</template>

<style scoped>
#text {
    color: var(--text);
}
</style>