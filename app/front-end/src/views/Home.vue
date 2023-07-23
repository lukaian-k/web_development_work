<script setup>
import { reactive } from 'vue'
import Title from '../components/Title.vue';
import { useStore } from 'vuex'
import router from "../router"

const store = useStore()

if (!store.state.isAuthenticated) {
    router.push('/sign-in')
}

const itens = reactive([
    { name: 'Cursos', route: '/courses' },
    { name: 'Professores', route: '/professors' },
    { name: 'Sala de Aula', route: '/classrooms' },
    { name: 'Alocação', route: '/allocation' }
])
</script>

<template>
    <Title hType="h1" text="Página Inicial" />
    <v-list>
        <v-list-item id="btn" v-for="(item, i) in itens" :key="i" :value=item.name color=var(--secondary-elements)
            rounded="xl" variant="outlined" max-width="500" class="mx-auto pa-2">
            <RouterLink :to=item.route>
                <v-list-item-title id="text" v-text=item.name />
            </RouterLink>
        </v-list-item>
    </v-list>
</template>

<style scoped lang="scss">
$highlights: var(--highlights);
$secondary-elements: var(--secondary-elements);
$background: var(--background);

#btn {
    background-color: $highlights;
    margin: 15px;

    &:hover {
        background-color: $secondary-elements;
        transform: scale(1.02);
        transition: 200ms;
        border: none;
    }
}

#text {
    color: $background;
}
</style>
