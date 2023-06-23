<script>
export default {
    data: () => ({
        links: [
            'Cursos',
            'Professores',
            'Horários',
            'Sala de Aula',
            'Alocação',
        ],
    })
}
</script>

<template>
    <v-footer color=var(--background-gray)>
        <v-row justify="center" no-gutters>
            <v-btn v-for="link in links" :key="link" color=var(--text) variant="text" class="mx-2" rounded="xl">
                {{ link }}
            </v-btn>
            <v-col class="text-center mt-4" cols="12">
                © {{ new Date().getFullYear() }} — <strong>UFC Academic Manager.</strong> Todos os direitos reservados.
            </v-col>
        </v-row>
    </v-footer>
</template>