<script setup>
import { RouterLink } from 'vue-router'

defineProps({
    items: {
        type: Array,
        required: true
    }
})
</script>

<template>
    <div class="options">
        <v-col cols="12" sm="6" md="4" v-for="i in items">
            <RouterLink :to="i.router">
                <v-card class="option-card">
                    <v-card-title>{{ i.title }}</v-card-title>
                </v-card>
            </RouterLink>
        </v-col>
    </div>
</template>

<style scoped lang="scss">
$background: var(--background);
$background-gray: var(--background-gray);

.options {
    margin-top: 2rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .option-card {
        cursor: pointer;
        text-align: center;
        padding: 2rem;
        background-color: $background;
        transition: background-color 0.3s;

        &:hover {
            background-color: $background-gray;
        }
    }
}
</style>