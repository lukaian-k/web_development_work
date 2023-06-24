<script setup>
defineProps({
    hType: {
        type: String,
        required: true
    },
    text: {
        type: String,
        required: true
    }
})
</script>

<template>
    <component id="h-x" :is=hType>{{ text }}</component>
</template>

<style scoped>
#h-x {
    line-height: 1.1;
    color: var(--secondary-elements);
    margin-bottom: 20px;
    text-transform: uppercase;
    text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.2);
}
</style>