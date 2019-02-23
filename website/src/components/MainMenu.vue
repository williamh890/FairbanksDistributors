<template>
  <v-container fill-height class="size">
      <v-container>
          <v-layout
          align-center
          column>
              <v-flex>
                  <h1 class="font-weight-bold mb-3"> Main Menu </h1>
                      <v-btn
                          color="primary"
                          v-on:click="$emit('createOrder')">
                          Create Order
                      </v-btn>
              </v-flex>
              <v-flex>
                      <v-btn
                          color="primary">
                          Edit Order
                      </v-btn>
              </v-flex>
              <v-flex>
                      <v-btn
                          color="primary">
                          Settings
                      </v-btn>
              </v-flex>
              <v-flex>
                      <v-btn
                          color="primary"
                          v-on:click="$emit('Logout')">
                          Logout
                      </v-btn>
              </v-flex>
          </v-layout>
      </v-container>
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
