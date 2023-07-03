<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
    <div class="background">
        <h1 class="message">Em Desenvolvimento</h1>
        <RouterLink to="/">
            <v-btn id="btn">Voltar ao ínicio</v-btn>
        </RouterLink>
    </div>
</template>
  
<style scoped lang="scss">
#btn {
    margin-top: 1.5em;
}

.background {
    position: relative;
    width: 100%;
    height: 100vh;
    background-image: url('../assets/development-page.svg');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}

.message {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 3rem;
    font-weight: bold;
    color: white;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    text-align: center;
}
</style>
  