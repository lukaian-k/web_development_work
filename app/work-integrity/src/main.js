import { createApp } from 'vue'
import App from './App.vue'
import './style.scss'

import axios from 'axios'
import router from './router'
import vuetify from './plugins/vuetify'

const app = createApp(App)

const api = axios.create({
    baseURL: 'http://localhost:8000',
})
app.config.globalProperties.$http = api

app.use(router)
app.use(vuetify)

app.mount('#app')