import Vue from 'vue'
import VueRouter from 'vue-router'
import VueDemo from '@/components/VueDemo'
import LoginForm from '@/components/LoginForm'
import Messages from '@/components/Messages'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'home',
      component: LoginForm
    },
    {
      path: '/messages',
      component: Messages
    },
    {
      path: '/login',
      component: LoginForm
    }
  ]
})
