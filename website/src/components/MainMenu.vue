<template>
  <v-container fill-height class="size">
      <v-container>
          <v-layout
          align-space-around
          text-xs-center
          pa-5
          column>
              <template v-for="type of orderTypes">
                  <v-flex>
                      <v-btn round block large dark color="primary"
                              @click="onOrderTypeSelected(type)">{{type}} Order
                      </v-btn>
                  </v-flex>
              </template>

              <v-divider style="margin: 10px 0"></v-divider>

              <v-flex>
                <v-btn round block large dark
                  v-on:click=spreadsheetUpload
                  color=info>
                   Update Order Items
                </v-btn>
              </v-flex>
              <v-flex>
                <v-btn round block large dark
                  color=info>
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
import { CLEAR_ORDER_ITEMS, CLEAR_ORDER_SETTINGS, SET_ORDER_TYPE } from "../store/orders/mutation";

export default {
  name: 'MainMenu',
  store,
  computed: {
    orderTypes() {
        return this.$store.getters.getOrderTypes;
    },
  },
  methods:    {
    newOrder: function () {
      this.$store.dispatch(CLEAR_ORDER_ITEMS);
      this.$store.dispatch(CLEAR_ORDER_SETTINGS);
      this.$emit('createOrder');
    },
    spreadsheetUpload: function() {
      this.$emit('spreadsheetUpload');
    },
    onOrderTypeSelected: function(type) {
        this.$store.dispatch(SET_ORDER_TYPE, type);
        this.newOrder()
    },
  }
}
</script>

<style>
.size {
  max-width: 100%;
  width: 600px;
}
</style>
