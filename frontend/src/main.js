// src/main.js
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { createPinia } from "pinia";

const app = createApp(App);

// Plugins
app.use(router); // Ajout du routeur
app.use(createPinia()); // Ajout de Pinia pour le store

// Montage de l'application
app.mount("#app");
