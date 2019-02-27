import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import 'vuetify/src/stylus/app.styl'

Vue.use(Vuetify, {
  iconfont: 'md',
  theme: {
    primary: '#142672',
    secondary: '#424242',
    accent: '#ED1B24',
    error: '#b71c1c'
  }
})
