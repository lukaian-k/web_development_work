<script setup>
import response from './myfile.json'
</script>

<template>
    <p v-for="i in response.Blocos">{{ i }}</p>
</template>

<style scoped lang="scss"></style>