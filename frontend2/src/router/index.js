import Vue from 'vue'
import VueRouter from 'vue-router'

import SignPage from '@/views/SignPage'
import MainPage from '@/views/MainPage'
import MoviePage from '@/views/MoviePage'
import ProfilePage from '@/views/ProfilePage'
import CategoryPage from '@/views/CategoryPage'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: MainPage, name: 'Home' },
    { path: '/sign', component: SignPage, name: 'Sign' },
    { path: '/movie', component: MoviePage, name: 'Movie' },
    { path: '/search', component: CategoryPage, name: 'Search'},
    { path: '/profile', component: ProfilePage, name: 'Profile' },
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router
