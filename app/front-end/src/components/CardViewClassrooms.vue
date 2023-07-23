<script setup>
defineProps({
    sala: {
        type: Object,
        required: true,
    }
})
</script>

<template>
    <div class="card">
        <h3>{{ sala.nome }}</h3>
        <p>Capacidade: {{ sala.capacidade }}</p>
        <p>Bloco: {{ sala.bloco }}</p>
    </div>
</template>
  
<style scoped lang="scss">
.card {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 16px;
    margin-bottom: 16px;
    background-color: var(--background);
    color: #020202;

    h3 {
        margin-top: 0;
    }

    p {
        margin-bottom: 8px;
    }
}
</style>
  