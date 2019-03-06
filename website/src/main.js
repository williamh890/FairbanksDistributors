import Vue from 'vue'
import './plugins/vuetify'
import './plugins/vue-rx'
import './plugins/vuex'
import './plugins/vue-resource'
import App from './App.vue'

import store from './store';

Vue.config.productionTip = false

new Vue({
  store,

  http: {
      root: '/',
      headers: {
        Authorization: 'Basic YXBpOnBhc3N3b3Jk'
      }
  },
  render: h => h(App),
}).$mount('#app')
