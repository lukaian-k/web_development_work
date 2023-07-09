<script setup>
import Title from '../../components/Title.vue';

let form = false
let loading = false

function onSubmit() {
    if (!this.form) return

    this.loading = true
    setTimeout(() => (this.loading = false), 2000)
}
</script>

<template>
    <Title hType="h1" text="Cadastro Professores" />

    <v-sheet width="800" class="mx-auto">
        <v-container fluid>
            <v-form fast-fail v-model=form @submit.prevent=onSubmit>
                <v-text-field required label="Nome" variant="outlined" />
                <v-text-field required label="Departamento" variant="outlined" />

                <v-container fluid>
                    <v-row class="container">
                        <v-text-field required type="number" label="Código" variant="outlined" />
                        <v-text-field class="element" required label="Formação" variant="outlined" />
                    </v-row>
                </v-container>

                <br>

                <v-btn :loading=loading :disabled=!form block color=var(--highlights) type="submit" variant="elevated"
                    rounded="xl" size="large">
                    <p id="text-send">Cadastrar</p>
                </v-btn>
            </v-form>
        </v-container>
    </v-sheet>
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