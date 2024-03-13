import { createRouter, createWebHistory } from 'vue-router';
import Navbar from '@/components/Navbar.vue';
import Body from '@/components/Body.vue';
import Comments from '@/components/Comments.vue';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'index',
            component: Navbar, Body, Comments
        },
    ]
});

export default router;