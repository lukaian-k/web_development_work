<script setup>
import Header from '../components/Login/Header.vue'
import Form from '../components/Login/Form.vue'
</script>

<template>
  <div class="login-page">
    <Header />
    <div class="login-form-container">
      <Form />
    </div>
    <div class="background"></div>
  </div>
</template>

<style scoped lang="scss">
$highlights: var(--highlights);

.login-page {
  display: flex;
  height: 100vh;
}

.login-form-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
}

.background {
  flex: 1.1;
  background-color: $highlights;
  background-image: url('../assets/img-login.svg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
}
</style>