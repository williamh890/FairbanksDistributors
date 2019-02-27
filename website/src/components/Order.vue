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
        <v-stepper-step :complete="element > 4" step="4">Success</v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <OrderSettings />
          <v-btn
            round
            bottom
            large
            color="primary"
            style="margin: auto -10px"
            @click="element =2"
            fixed
          >
            Continue
          </v-btn>
        </v-stepper-content>
        <v-stepper-content step="2">
          <OrderCreate />
          <v-btn
            round
            large
            bottom
            color="Primary"
            style="margin: auto -10px"
            v-on:click="element = 1"
            fixed
          >
            Back
          </v-btn>
          <v-btn
            round
            large
            bottom
            color="primary"
            style="margin: auto 100px"
            v-on:click="element = 3"
            fixed
          >
            Review Order
          </v-btn>
        </v-stepper-content>

        <v-stepper-content step="3">
          <OrderReview />
          <v-btn
            round
            large
            color="Primary"
            style="margin: auto -10px"
            v-on:click="element = 2"
            bottom
            fixed
          >
            Back
          </v-btn>
          <v-btn
            round
            large
            color="primary"
            style="margin: auto 100px"
            v-on:click="onSubmitOrder(order)"
            bottom
            fixed
          >
            <template>
              Submit Order
            </template>
          </v-btn>
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
    order() {
      return this.$store.getters.getOrder;
    }
  },
  data() {
    return {
      element: 0,
      isLoading: false,
      resp: null,
    };
  },
  methods: {
    onSubmitOrder(order) {
      this.isLoading = true;

      const formData = new FormData();
      formData.append('order', JSON.stringify(order));

      this.$http.post('https://backend.uafhalpost.net/place_order', formData)
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
