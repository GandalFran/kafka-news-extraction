import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/news/:id',
    name: 'NewsList',
    component: () => import('../views/NewsList.vue')
  },
  {
    path: '/news/detail/:id',
    name: 'NewsDetail',
    component: () => import('../views/NewsDetail.vue')
  }
];

const router = new VueRouter({
  routes
});

export default router;
