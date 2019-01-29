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
    </v-toolbar>

    <v-content>
      <Login/>
    </v-content>
  </v-app>
</template>

<script>
import Login from './components/Login'

export default {
  name: 'App',
  components: {
    Login
  },
  data () {
    return {
      //
    }
  }
}
</script>

<style>
</style>
