<template>
<div>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="username"
      label="Username"
      required
    ></v-text-field>

    <v-text-field
      v-model="password"
      label="Password"
      required
      type="password"
    ></v-text-field>

    <v-btn
      block
      :disabled="!valid"
      color="secondary"
      @click="validate"
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
    username: '',
    password: '',
  }),

  methods: {
    validate () {
      if (this.$refs.form.validate()) {
        this.snackbar = true
      }
    },
  }
}
</script>

<style>

</style>
