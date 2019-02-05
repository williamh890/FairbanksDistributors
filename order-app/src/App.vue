<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Fairbanks Distributors</span>
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
      <Order v-else/>
    </v-content>
  </v-app>
</template>

<script>
import Login from './components/Login';
import Order from './components/Order';

export default {
  name: 'App',
  components: {
    Login,
    Order
  },
  methods: {
    onLoggin: function() {
      this.isLoggedIn = true;
    },
    onLogout: function() {
      this.isLoggedIn = false;
    }
  },
  data () {
    return {
      isLoggedIn: false
    }
  }
}
</script>

<style>
</style>
