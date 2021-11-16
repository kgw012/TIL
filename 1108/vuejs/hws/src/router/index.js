import Vue from 'vue'
import VueRouter from 'vue-router'
import Lunch from '../views/Lunch.vue'
import Lotto from '../views/Lotto.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/lunch',
    name: 'Lunch',
    component: Lunch
  },
  {
    path: '/lotto/:lottoNum',
    name: 'Lotto',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Lotto,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
