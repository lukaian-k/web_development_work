<script setup>
import { RouterLink } from 'vue-router'
import { useStore } from 'vuex'
import { ref } from 'vue'
import axios from 'axios'
import router from "../../router"

let form = ref(false)
let id = ref(null)
let password = ref(null)
let visible = ref(false)
let loading = ref(false)

const store = useStore()
console.log(store.state.isAuthenticated)

async function onSubmit() {
  if (!form) return

  loading = true
  setTimeout(() => (loading = false), 2000)

  axios.post('http://localhost:8000/login/', {
    id_user: id.value,
    password: password.value
  })
    .then(res => {
      store.commit('SET_AUTHENTICATED', true)
      store.commit('SET_USER', res.data)

      router.push('/home')
    })
    .catch(error => {
      console.error('Erro:', error)

      alert('Não foi possível efetuar o login.')
      id.value = ''
      password.value = ''
    })
}

function required(v) {
  return !!v || 'Campo nessesário'
}
</script>

<template>
  <v-form class="empty-form" v-model=form @submit.prevent=onSubmit>
    <div id="title">
      <h1>Bem-vindo!</h1>
      <p>Insira todas as informações corretamente para efetuar o login.</p>
    </div>

    <v-text-field v-model=id type="number" :readonly=loading :rules=[required] label="ID" variant="outlined"
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