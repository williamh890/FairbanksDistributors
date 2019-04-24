<template>
  <v-container fill-height class="size">
      <v-container>
          <v-layout
          align-space-around
          text-xs-center
          pa-5
          column>
              <v-flex>
                <v-btn round block large dark
                  color=primary
                  v-on:click=newOrder>
                    Create Order
                </v-btn>
              </v-flex>
              <v-flex>
                <v-btn round disabled block large dark
                  v-on:click=spreadsheetUpload
                  color=primary>
                   Update Order Items
                </v-btn>
              </v-flex>
              <v-flex>
                <v-btn round block large dark
                  color=primary>
                    Settings
                </v-btn>
              </v-flex>
              <v-flex>
                <v-btn round block large dark
                  color=secondary
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
import { CLEAR_ORDER_ITEMS, CLEAR_ORDER_SETTINGS } from "../store/orders/mutation";

export default {
  name: 'MainMenu',
  store,
  methods:    {
    newOrder: function () {
      this.$store.dispatch(CLEAR_ORDER_ITEMS);
      this.$store.dispatch(CLEAR_ORDER_SETTINGS);
      this.$emit('createOrder');
    },
    spreadsheetUpload: function() {
      this.$emit('spreadsheetUpload');
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
