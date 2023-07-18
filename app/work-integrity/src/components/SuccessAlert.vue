<script setup>
defineProps({
    isShow: {
        type: Boolean,
        required: true,
    },
    msg: {
        type: String,
        required: true,
    }
})
</script>

<template>
    <v-card class="success-card" v-if="isShow">
        <v-card-text>{{ msg }}</v-card-text>
        <v-card-actions>
            <v-btn color="var(--highlights)" @click="isShow = false">Fechar</v-btn>
        </v-card-actions>
    </v-card>
</template>
  
<style scoped lang="scss">
.success-card {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 300px;
}
</style>