import { createApp } from 'vue'
import { createPinia } from 'pinia'

import PrimeVue from 'primevue/config'
import 'primevue/resources/themes/aura-light-green/theme.css'
import 'primeflex/primeflex.min.css'
import 'primeicons/primeicons.css'

import App from '@/App.vue'
import router from '@/router'

import '@/assets/main.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.use(PrimeVue)

app.mount('#app')
