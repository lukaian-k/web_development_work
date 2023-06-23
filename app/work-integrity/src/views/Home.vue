<script>
export default {
    data: () => ({
        items: [
            { name: 'Cursos', route: '/courses' },
            { name: 'Professores', route: '/professors' },
            { name: 'Horários', route: '/schedules' },
            { name: 'Sala de Aula', route: '/classrooms' },
            { name: 'Alocação', route: '/allocation' }
        ]
    })
}
</script>

<template>
    <v-list>
        <v-list-item id="btn" v-for="(item, i) in items" :key="i" :value=item.name color=var(--secondary-elements)
            rounded="xl" variant="outlined" max-width="500" class="mx-auto pa-2">
            <RouterLink :to=item.route>
                <v-list-item-title id="text" v-text=item.name />
            </RouterLink>
        </v-list-item>
    </v-list>
</template>

<style scoped>
#btn {
    background-color: var(--highlights);
    margin: 15px;
}

#btn:hover {
    background-color: var(--secondary-elements);
    transform: scale(1.02);
    transition: 200ms;
    border: none;
}

#text {
    color: var(--background);
}
</style>
