import { fileURLToPath, URL } from 'node:url';
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import vuetify from 'vite-plugin-vuetify';
import vueDevTools from 'vite-plugin-vue-devtools';

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
    vuetify({ autoImport: true }),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      '@fullcalendar/core': fileURLToPath(new URL('./node_modules/@fullcalendar/core', import.meta.url)),
      '@fullcalendar/core/internal': fileURLToPath(new URL('./node_modules/@fullcalendar/core/internal.js', import.meta.url)),
      '@fullcalendar/core/preact': fileURLToPath(new URL('./node_modules/@fullcalendar/core/preact.js', import.meta.url)),
    },
  },
  optimizeDeps: {
    include: [
      '@fullcalendar/core',
      '@fullcalendar/vue3',
      '@fullcalendar/daygrid',
      '@fullcalendar/timegrid',
      '@fullcalendar/interaction',
    ],
  },
});
