/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

// Plugins
import { registerPlugins } from '@/plugins'
import DocumentPage from "@/views/DocumentPage.vue";
import RunPage from "@/views/RunPage.vue";
import LandingPage from "@/views/LandingPage.vue";
import IrDatasetsExplorer from "@/views/IrDatasetsExplorer.vue";
import Milestones from "@/views/Milestones.vue";
import { useDisplay } from 'vuetify'

export function is_mobile() {
    const { mobile } = useDisplay()
    return mobile.value
}

export default function register_app() {
    const app_selector = '#app'

    const app_elem = document.querySelector(app_selector)
    if (app_elem && '__vue_app__' in app_elem && app_elem.__vue_app__) {
      console.log('App is already mounted.')
      return;
    }

    console.log('Mount vue app to location: ' + window.location)

    const routes = [
      {path: '/', component: LandingPage},
      {path: '/topics', component: IrDatasetsExplorer, name: 'Browse Topics'},
      {path: '/ir-lab-sose-24/topics', component: IrDatasetsExplorer, name: 'Browse Topics'},
      {path: '/milestones', component: Milestones, name: 'Milestones'},
      {path: '/ir-lab-sose-24/milestones', component: Milestones, name: 'Milestones'},
      {path: '/docs', component: DocumentPage},
      {path: '/ir-lab-sose-24/docs', component: DocumentPage, name: 'Browse Documents'},
      {path: '/runs', component: RunPage},
      {path: '/ir-lab-sose-24/runs', component: RunPage, name: 'Browse runs'},

      // Fallback: everything matches to home.
      {path: '/:pathMatch(.*)*', component: LandingPage},
    ]

    const router = createRouter({
      history: createWebHistory(),
      routes,
    })

    const app = createApp(App)
    app.use(router)

    registerPlugins(app)

    app.mount(app_selector)
}

declare global { interface Window { register_app: any}}
window.register_app = register_app;

register_app()
