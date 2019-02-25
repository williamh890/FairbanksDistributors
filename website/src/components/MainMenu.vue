<template>
  <v-container fill-height class="size">
      <v-container>
          <v-layout
          align-space-around
          text-xs-center
          pa-5
          column>
              <v-flex>
                  <h1 class="display-1 font-weight-bold mb-4"> Main Menu </h1>
              </v-flex>
              <v-flex>
                      <v-btn
                          round
                          block
                          large
                          color=rgba(21,38,112)
                          dark
                          v-on:click=newOrder>
                          Create Order
                      </v-btn>
              </v-flex>
              <v-flex>
                      <v-btn
                          round
                          block
                          large
                          color=rgba(21,38,112)
                          dark>
                          Edit Order
                      </v-btn>
              </v-flex>
              <v-flex>
                      <v-btn
                          round
                          block
                          large
                          color=rgba(21,38,112)
                          dark>
                          Settings
                      </v-btn>
              </v-flex>
              <v-flex>
                      <v-btn
                          round
                          block
                          large
                          color=secondary
                          dark
                          v-on:click="$emit('Logout')">
                          Logout
                      </v-btn>
              </v-flex>
          </v-layout>
      </v-container>
  </v-container>
</template>

<script>
import store from '../store';
import { CLEAR_ORDER_ITEMS } from "../store/orders/mutation";

export default {
    name: 'MainMenu',
    store,
    methods:    {
        newOrder: function () {
            this.$store.dispatch(CLEAR_ORDER_ITEMS);
            this.$emit('createOrder')
        }
    }
}
</script>

<style>
.size {
  max-width: 100%;
  width: 600px;
}
</style>
