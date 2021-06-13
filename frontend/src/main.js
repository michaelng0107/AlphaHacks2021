import { createApp } from 'vue'
// import App from './App.vue'
import router from './router'
import index from './views/index.vue'

createApp(index).use(router).mount('body')
