<template>
  <v-container class="size">
    <v-layout
      text-xs-center
      wrap
    >
      <v-flex xs12>
        <h1 class="display-2 font-weight-bold mb-3">
            Login
        </h1>

        <v-img
          :src="require('../assets/chips.jpg')"
          class="my-3"
          contain
          height="200"
        ></v-img>
      </v-flex>

      <v-flex mb-4>

        <LoginForm />

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
