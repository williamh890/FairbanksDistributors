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
        <v-stepper-step :complete="element > 4" step="4">Add Notes</v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step :complete="element > 5" step="5">Success</v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <OrderSettings />
        </v-stepper-content>
        <v-stepper-content step="2">
          <OrderCreate />
        </v-stepper-content>
        <v-stepper-content step="3">
          <OrderReview />
        </v-stepper-content>
        <v-stepper-content step="4">
          <OrderNotes />
        </v-stepper-content>
        <v-stepper-content step="5">
          <OrderSuccess />

          <div v-if="resp">
            <!--{{ JSON.stringify(resp) }}-->
          </div>
        </v-stepper-content>
      </v-stepper-items>

      <v-snackbar v-model="unselectedSettingsNotifier" :timeout="3000" :color="color">
        {{ text }}
      </v-snackbar>
      <v-footer fixed height="auto">
        <v-btn color="primary" :disabled="element === 1" flat large @click="element--">
          <v-icon>arrow_back</v-icon>
          Back
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn color="primary" v-if="element <= 3" flat large @click="this.canProgress" right>
          Next
          <v-icon>arrow_forward</v-icon>
        </v-btn>
        <v-btn color="primary" v-if="element === 4" flat large v-bind:loading="this.isLoading" @click="onSubmitOrder(order)">
          Submit Order
        </v-btn>
      </v-footer>
    </v-stepper>
  </v-container>
</template>

<script>
import OrderSettings from './OrderSettings';
import OrderCreate from './OrderCreate';
import OrderReview from './OrderReview';
import OrderNotes from './OrderNotes';
import OrderSuccess from './OrderSuccess';
import store from '../store';

export default {
  name: 'Order',
  store,
  components: {
    OrderSettings,
    OrderCreate,
    OrderReview,
    OrderNotes,
    OrderSuccess,
  },
  computed: {
    order() {
      return this.$store.getters.getOrder;
    }
  },
  data() {
    return {
      element: 1,
      isLoading: false,
      resp: null,
      unselectedSettingsNotifier: false,
      color: "error",
      text: "Please select all settings."
    };
  },
  methods: {
    canProgress() {
      if (this.$store.getters.getOrderDate != null && this.$store.getters.getDeliveryLocation != null){
        this.element++
      }
      else {
        this.unselectedSettingsNotifier=true
      }
    },
    onSubmitOrder(order) {
      this.isLoading = true;

      const formData = new FormData();
      formData.append('order', JSON.stringify(order));

      const apiUrl = 'https://1ovq6hhh55.execute-api.us-west-2.amazonaws.com/production/place_order';
      this.$http.post(apiUrl, formData)
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
