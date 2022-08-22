import { createRouter, createWebHashHistory } from 'vue-router'
import Layout from '@/views/Layout.vue'
import Home from '@/views/Home/Home.vue'
const Login=()=>import('@/views/Login.vue')
const About=()=>import('@/views/About.vue')
const HomeView=()=>import('@/views/HomeView.vue')
const HomeView2=()=>import('@/views/HomeView2.vue')
const twoMethods=()=>import('@/views/twoMethods.vue')
const user=()=>import('@/views/user')
const bye=()=>import('@/views/bye')

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
  },{
    path: '/homeview2',
    component:HomeView2
  },{
    path: '/twomethods',
    component:twoMethods
  },{
    path: '/user',
    component:user
  },{
    path: '/bye',
    component:bye
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
