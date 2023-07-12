<script setup>
defineProps({
    list: {
        type: Array,
        required: true,
    }
})
</script>

<template>
    <div class="card-container">
        <div v-for="i in list" class="card">
            <div class="card-content">
                <span class="card-title">{{ i }}</span>
            </div>
        </div>
    </div>
</template>
  
<style scoped lang="scss">
.card-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 20px;
    padding: 20px;
}

.card {
    background-color: #f2f2f2;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    width: calc((100% - 40px) / 3);
    /* 3 colunas com espaçamento de 20px */
    height: 150px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.card-content {
    padding: 16px;
}

.card-title {
    font-size: 18px;
    font-weight: bold;
    color: #333;
}
</style>