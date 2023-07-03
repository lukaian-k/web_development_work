<script setup>
import Title from '../../components/Title.vue';

let form = false
let loading = false

let items = [
    'Projetor',
    'Caixa de som',
    'Câmera',
    'Microfone',
]

function onSubmit() {
    if (!this.form) return

    this.loading = true
    setTimeout(() => (this.loading = false), 2000)
}
</script>

<template>
    <Title hType="h1" text="Cadastro de Salas de Aula" />

    <v-sheet width="800" class="mx-auto">
        <v-container fluid>
            <v-form fast-fail v-model=form @submit.prevent=onSubmit>
                <v-text-field required type="number" label="Número da Sala" />
                <v-text-field required type="number" label="Capacidade" />
                <v-text-field required label="Bloco" />
                <v-combobox :items=items label="Dispositivos eletrônicos" multiple chips></v-combobox>

                <br>

                <v-btn :loading=loading :disabled=!form block color=var(--highlights) type="submit" variant="elevated"
                    rounded="xl" size="large">
                    <p id="text-send">Cadastrar</p>
                </v-btn>
            </v-form>
        </v-container>
    </v-sheet>
</template>

<style scoped>
#text-send {
    color: var(--background);
}
</style>