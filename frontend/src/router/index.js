import { createRouter, createWebHashHistory } from 'vue-router';
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue';
import index from '../views/index.vue';

const routes = [
	{
		path: '/',
		name: 'index',
		component: index
	},
	{
		path: '/about',
		name: 'About',
		// route level code-splitting
		// this generates a separate chunk (about.[hash].js) for this route
		// which is lazy-loaded when the route is visited.
		component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
	}
]

const router = createRouter({
  history: createWebHashHistory(''),
  mode: 'history',
  routes,

})

export default router
