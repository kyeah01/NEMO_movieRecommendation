import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// fontawesome
import { library } from '@fortawesome/fontawesome-svg-core'
import {fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(fas, far, fab)
Vue.component('fa-icon', FontAwesomeIcon)
// end
Vue.prototype.$EventBus = new Vue()
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
