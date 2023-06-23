import { createApp } from 'vue'
import { createVuetify } from 'vuetify'

import App from './App.vue'
import router from './router'

import './style.css'
import 'vuetify/styles'
import * as directives from 'vuetify/directives'
import * as components from 'vuetify/components'

const app = createApp(App)
const vuetify = createVuetify({
    components,
    directives,
})

app.use(router)
app.use(vuetify)

app.mount('#app')