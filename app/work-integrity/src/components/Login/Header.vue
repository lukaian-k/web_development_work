<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
    <nav class="app-bar">
        <RouterLink to="/">
            <img id="app-bar-icon" src="../../assets/icon-ufc.svg" alt="icone da UFC">
        </RouterLink>

        <span class="sign-up">
            <v-btn variant="outlined" rounded="xl">Sign Up</v-btn>
        </span>
    </nav>
</template>

<style scoped lang="scss">
.app-bar {
    display: flex;
    align-items: center;
    background-color: transparent;
    position: absolute;
    inset: 0 0 auto 0;

    #app-bar-icon {
        margin-top: 1em;
        margin-left: 2em;
    }

    .sign-up {
        flex-grow: 1;
        display: flex;
        justify-content: flex-end;
        color: var(--background);
        margin-top: 1em;
        margin-right: 1.5em;
    }
}
</style>