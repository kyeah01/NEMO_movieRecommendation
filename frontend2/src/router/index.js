import Vue from 'vue'
import VueRouter from 'vue-router'

import SignPage from '@/views/SignPage'
import MainPage from '@/views/MainPage'
import MoviePage from '@/views/MoviePage'
import ProfilePage from '@/views/ProfilePage'
import NewRatingPage from '@/views/NewRatingPage'
import CategoryPage from '@/views/CategoryPage'
import AdminPage from '@/views/AdminPage'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: MainPage, name: 'Home' },
    { path: '/admin', component: AdminPage, name: 'Admin' },
    { path: '/newrating', component: NewRatingPage, name: 'NewRating' },
    { path: '/sign', component: SignPage, name: 'Sign' },
    { path: '/movie', component: MoviePage, name: 'Movie' },
    { path: '/search', component: CategoryPage, name: 'Search'},
    { path: '/profile', component: ProfilePage, name: 'Profile' },
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

router.beforeEach((to, from, next) => {
  console.log(to, from, next)
  if (to.name == 'Home' || to.name == 'Sign') {
    console.log(1)
    if (sessionStorage.hasOwnProperty('drf')) {
    console.log(2)
      return next('/movie')
    }
  } else {
    console.log(3)
    if (!sessionStorage.hasOwnProperty('drf')) {
    console.log(4)
      return next('/')
    }
  }
  return next()
})

export default router
