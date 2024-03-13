import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../src/HomePage.vue';
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'index',
            component: HomePage,
        },
    ]
});

export default router;