<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})

let num = ref(0)
</script>

<template>
  <form action="" method="post">
    <h2>{{ msg }}</h2>
    <label for="username"></label>
    <input type="text" name="username" id="username">
    <label for="password"></label>
    <input type="password" name="password" id="password">
    <button type="submit">Send</button>
  </form>
</template>

<style scoped></style>
