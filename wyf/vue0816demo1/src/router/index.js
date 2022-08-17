import { createRouter, createWebHashHistory } from 'vue-router'
import Layout from '@/views/Layout.vue'
import Home from '@/views/Home/Home.vue'
const Login=()=>import('@/views/Login.vue')

const routes = [
  {
    path: '/',
    name:'Layout',
    component: Layout,
    children:[
      {
        path: '/',
        component:Home  
      }
    ]
  },{
    path: '/login',
    component:Login
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
