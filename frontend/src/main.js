import { createApp } from 'vue'
import App from './App.vue'
import router from './router'   // import do Router
const app = createApp(App)

app.use(router)  // registra o Vue Router na aplicação
app.mount('#app')