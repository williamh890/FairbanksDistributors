<template>
  <v-container class="size" fluid grid-list-xl>
    <v-stepper v-model="element">
      <v-stepper-header>
        <v-stepper-step :complete="element > 1" step="1">Create</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step :complete="element > 2" step="2">Review</v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <OrderCreate />

            <v-btn
              block
              color="secondary"
              style="margin-top: 10px"
              v-on:click="element = 2"
            >
              Submit Order
            </v-btn>
        </v-stepper-content>

        <v-stepper-content step="2">
          <v-card
            class="mb-5"
            color="grey lighten-1"
            height="200px"
          ></v-card>

          <v-btn
            color="primary"
            @click="element = 2"
          >
            Submit
          </v-btn>

          <v-btn flat
            @click="element = 1"
            >Previous</v-btn>
      </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </v-container>
</template>

<script>
import OrderCreate from './OrderCreate';
import store from '../store';
import { SET_SELECTED_ITEM_TYPE, ADD_ORDER_ITEM } from '../store/orders/mutation';

export default {
  name: 'Order',
  components: {
    OrderCreate
  },
  data() {
    return {
      element: 0
    };
  }
}
</script>

<style>
.size {
  max-width: 100%;
  width: 600px;
}
</style>
