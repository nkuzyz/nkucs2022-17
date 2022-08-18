import { createRouter, createWebHashHistory } from 'vue-router'
import Layout from '@/views/Layout.vue'
import Home from '@/views/Home/Home.vue'
const Login=()=>import('@/views/Login.vue')
const About=()=>import('@/views/About.vue')
const HomeView=()=>import('@/views/HomeView.vue')

const routes = [
  {
    path: '/',
    name:'Layout',
    component: Layout,
    // children:[
    //   {
    //     path: '/',
    //     component:Home
    //   }
    // ]
  },{
    path: '/login',
    component:Login
  },{
    path: '/about',
    name:'About',
    component:About
  },{
    path: '/homeview',
    component:HomeView
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
