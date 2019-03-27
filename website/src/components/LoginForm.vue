<template>
<div>
  <v-form
    ref="form"
    v-model="valid"
    v-on:submit.prevent="login()"
    lazy-validation
  >
    <v-text-field
      v-model="password"
      label="Password"
      :rules="passwordRules"
      :error-messages="passwordError"
      required
      v-on:keydown="clearErrors()"
      type="password"
    ></v-text-field>

    <v-btn
      block
      :disabled="!valid"
      color="secondary"
      v-on:click="login()"
    >
      Login
    </v-btn>
  </v-form>
</div>
</template>

<script>
import { apiUrl } from '../data/api';

export default {
  name: 'LoginForm',
  data: () => ({
    valid: true,
    password: '',
    passwordError: [],
    passwordRules: [
      v => !!v || 'Password is required',
    ]
  }),

  methods: {
    login () {
      const password = this.password;
      const url = `${apiUrl}/login?auth_key=${password}`;
      this.$http.get(url)
        .then(resp => {
          this.$emit('login', password);
        })
        .catch(_ => {
          this.passwordError = ['Password is not valid.'];
        });
    },
    clearErrors() {
      this.passwordError = [];
    }
  }
}
</script>

<style>

</style>
