import Vue from 'vue'
import Vuex from 'vuex'
import mutations from './mutations'
import getters from './getters'
import actions from './actions'
import axios from 'axios'

// Make Axios play nice with Django CSRF
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieSearchList: [],
    movieUserList: [],
    userData: [],
    selectedMovie: {
      'Activated': null,
      'ActivatedMovie': null,
      'selectedInfo': 1,
    },
    userData: [],
    
    // JWT
    authUser: {},
    isAuthenticated: false,
    jwt: sessionStorage.getItem('token'),
    endpoints: {
      // TODO: Remove hardcoding of dev endpoints
      // obtainJWT: 'auth',
      // refreshJWT: 'http://127.0.0.1:8000/api/v1/auth/refresh/',
      // baseUrl: 'http://127.0.0.1:8000/api/auth/'
    }

  },
  mutations,
  getters,
  actions
})
