<template>
  <v-container class="size">
    <v-layout
      text-xs-center
      wrap
    >
      <v-flex xs12>
        <v-img
          :src="require('../../../images/FD_Logo.png')"
          class="my-3"
          contain
          height="200"
        ></v-img>

        <h1 class="display-2 font-weight-bold mb-3">
            Login
        </h1>
      </v-flex>

      <v-flex mb-4>

        <LoginForm
          v-on:login="$emit('login')"
        />

      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import LoginForm from './LoginForm.vue';

export default {
  name: 'Login',
  components: {
    LoginForm
  },
}
</script>

<style>
.size {
  width: 40%;
  min-width: 300px;
  max-width: 600px;
}
</style>
