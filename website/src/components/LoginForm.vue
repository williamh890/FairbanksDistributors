<template>
<div>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="password"
      label="Password"
      :rules="passwordRules"
      :error-messages="passwordError"
      required
      v-on:change="clearErrors()"
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
      const apiUrl = `http://localhost:5000/login?auth_key=${password}`;
      this.$http.get(apiUrl)
        .then(resp => {
          this.$emit('login', password);
        })
        .catch(resp => {
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
