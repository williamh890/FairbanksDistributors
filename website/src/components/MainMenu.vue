<template>
  <v-container class="size">
      <v-layout
      text-xs-center
      wrap>
          <v-flex xs12>
              <h1 class="font-weight-bold mb-3"> Main Menu </h1>
              <v-btn
                  color="primary"
                  v-on:click="$emit('createOrder')">
                  Create Order
              </v-btn>
          </v-flex>
      </v-layout>
  </v-container>
</template>

<script>

export default {
  name: 'MainMenu',
}
</script>

<style>
.size {
  max-width: 100%;
  width: 600px;
}
</style>
