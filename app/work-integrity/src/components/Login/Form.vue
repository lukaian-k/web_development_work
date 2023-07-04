<script setup>
import { RouterLink } from 'vue-router'
import { ref } from 'vue'

let form = ref(false)
let id = ref(null)
let password = ref(null)
let visible = ref(false)
let loading = ref(false)

async function onSubmit() {
  if (!this.form) return

  this.loading = true
  setTimeout(() => (this.loading = false), 2000)

  try {
    const response = await this.$http.post('http://localhost:8000/api/sign-in/', {
      id_user: this.id,
      password: this.password,
    })

    alert(response)

  } catch (error) {
    console.log(error)
  }
}

function required(v) {
  return !!v || 'Campo nessesário'
}
</script>

<template>
  <v-form class="empty-form" v-model=form @submit.prevent=onSubmit>
    <div id="title">
      <h1>Bem-vindo!</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit</p>
    </div>

    <v-text-field v-model=id type="input" :readonly=loading :rules=[required] label="ID" variant="outlined"
      placeholder="Insira seu código de identificação" density="compact" />

    <v-text-field v-model=password :type="visible ? 'text' : 'password'" @click:append-inner="visible = !visible"
      :readonly=loading :rules=[required] label="Password" variant="outlined" hint="Insira sua senha" density="compact"
      :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'" />

    <br>

    <v-btn :disabled=!form :loading=loading block color=var(--highlights) type="submit" variant="elevated" rounded="xl"
      size="large">
      <p id="text-send">Entrar</p>
    </v-btn>

    <!-- <br><br>
    <p>
      Não tem uma conta?
      <RouterLink to="/">Sign in</RouterLink>
    </p> -->
  </v-form>
</template>

<style scoped lang="scss">
#title {
  margin-bottom: 2.5em;

  h1 {
    margin-bottom: .1em;
  }
}

.empty-form {
  min-width: 60%;
}

#text-send {
  color: var(--background);
}
</style>