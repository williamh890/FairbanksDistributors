<template>
  <v-app>
    <v-toolbar app
      v-if="isLoggedIn">
      <v-toolbar-items>
        <v-btn large icon
          v-on:click="goHome">
          <v-img
            :src="require('./assets/FD_Monogram.png')"
            contain
            ></v-img>
        </v-btn>
      </v-toolbar-items>
      <v-toolbar-title class="headline text-uppercase">
        <span>FD</span>
        <span class="font-weight-light ml-2" >ORDER APP</span>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn flat
         v-if="isLoggedIn"
         v-on:click="onLogout">
        Logout
      </v-btn>

    </v-toolbar>

    <v-content>
      <Login
        v-if="!isLoggedIn"
        v-on:login="onLoggin($event)"
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

import {
  LOGIN, LOGOUT, HIDEMAIN,
  SHOWMAIN, SET_ITEMS
} from './store/orders/mutation';

export default {
  name: 'App',
  store,
  components: {
    Login,
    MainMenu,
    Order
  },
  methods: {
    onLoggin: function(password) {
      const apiUrl = `http://localhost:5000/items/chips?auth_key=${password}`;

      this.$http.get(apiUrl)
        .then(resp => {
          const data = resp.body;
          let chips = [];

          for (const [chipType, items] of Object.entries(data)) {
            const withType = items
              .map(item => ({...item, type: chipType, amount: 0}));

            chips = [...chips, ...withType];
          }

          this.$store.dispatch(SET_ITEMS, chips);
          this.$store.dispatch(LOGIN, password);
        })
    },
    onLogout: function() {
      this.$store.dispatch(LOGOUT);
    },
    createOrder: function() {
      this.$store.dispatch(HIDEMAIN);
    },
    goHome: function() {
      this.$store.dispatch(SHOWMAIN);
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
