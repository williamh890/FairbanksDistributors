<template>
  <v-container class="size" fluid grid-list-xl>
    <v-stepper v-model="element">

      <v-stepper-header>
        <v-stepper-step :complete="element > 1" step="1">Settings</v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step :complete="element > 2" step="2">Create</v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step :complete="element > 3" step="3">Review</v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step :complete ="element > 4" step="4">Success</v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <OrderSettings />

            <v-btn
              color="primary"
              @click="element =2"
              >
              Continue
            </v-btn>
        </v-stepper-content>
        <v-stepper-content step="2">
          <OrderCreate />

            <v-btn
              block
              color="primary"
              style="margin-top: 10px"
              v-on:click="element = 3"
            >
              Review Order
            </v-btn>
          <v-btn flat
            @click="element = 1"
            >Back</v-btn>


        </v-stepper-content>

        <v-stepper-content step="3">
          <OrderReview />

          <v-btn
            color="primary"
            v-on:click="onSubmitOrder(orderItems)"
          >
            <template >
              Submit Order
            </template>
          </v-btn>

          <v-btn flat
            @click="element = 2"
            >Edit</v-btn>

            <v-progress-circular v-if="isLoading" indeterminate color="secondary" ></v-progress-circular>
      </v-stepper-content>
      <v-stepper-content step="4">
        <OrderSuccess />

        <div v-if="resp">
          {{ JSON.stringify(resp) }}
        </div>
      </v-stepper-content>

      </v-stepper-items>
    </v-stepper>
  </v-container>
</template>

<script>
import OrderSettings from './OrderSettings';
import OrderCreate from './OrderCreate';
import OrderReview from './OrderReview';
import OrderSuccess from './OrderSuccess';
import store from '../store';

export default {
  name: 'Order',
  store,
  components: {
    OrderSettings,
    OrderCreate,
    OrderReview,
    OrderSuccess,
  },
  computed: {
    orderItems() {
      return this.$store.getters.getOrderItems;
    }
  },
  data() {
    return {
      element: 0,
      isLoading: false,
      resp: null,
      date: new Date().toISOString().substr(0, 10),
      menu: false,
    };
  },
  methods: {
    onSubmitOrder(orderItems) {
      const items = orderItems.map(orderItem => {
        const { amount, ...item } = orderItem;

        return { amount, item };
      })

      this.isLoading = true;

      this.$http.get('https://backend.uafhalpost.net/place_order')
        .then(
          resp => {
            this.element = 4;
            this.isLoading = false;
            this.resp = resp;
          }
        );
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
