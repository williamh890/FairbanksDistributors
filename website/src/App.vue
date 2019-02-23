<template>
  <v-app>
    <v-toolbar app
    v-if="isLoggedIn">
      <v-toolbar-items>
        <v-img
            :src="require('../../images/FD_Monogram.png')"
            height="50"
            width="50"
            contain
        ></v-img>
      </v-toolbar-items>
      <v-toolbar-title class="headline text-uppercase">
        <span>FD</span>
        <span class="font-weight-light ml-2" >ORDER APP</span>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn flat>
        <v-icon>reorder</v-icon>
      </v-btn>
      <v-btn flat
         v-if="isLoggedIn"
         v-on:click="onLogout">
        Logout
      </v-btn>

    </v-toolbar>

    <v-content>
      <Login
        v-if="!isLoggedIn"
        v-on:login="onLoggin"
      />
      <MainMenu
        v-else-if="mainMenuActive"
        v-on:createOrder="createOrder"
        v-on:Logout="onLogout"
      />
      <Order v-else/>
    </v-content>
  </v-app>
</template>

<script>
import Login from './components/Login';
import Order from './components/Order';
import MainMenu from './components/MainMenu'
import store from './store';

import { LOGIN, LOGOUT, HIDEMAIN } from './store/orders/mutation';

export default {
  name: 'App',
  store,
  components: {
    Login,
    MainMenu,
    Order
  },
  methods: {
    onLoggin: function() {
      this.$store.dispatch(LOGIN);
    },
    onLogout: function() {
      this.$store.dispatch(LOGOUT);
    },
    createOrder: function() {
      this.$store.dispatch(HIDEMAIN);
    },
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.getIsLoggedIn;
    },
    mainMenuActive() {
      return this.$store.getters.getIsMainMenuActive;
    }
  }
}
</script>

<style>
</style>
