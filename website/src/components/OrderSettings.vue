<template>
    <v-container>
        <h1> Order Settings </h1>
        <v-select
      :items="storeNames"
      v-on:change="onStoreNameChanged"
      label="Store"
      ></v-select>
        <v-menu
          v-model="menu"
          :close-on-content-click="false"
          :nudge-right="40"
          lazy
          transition="scale-transition"
          offset-y
          full-width
          min-width="290px"
        >
          <v-text-field
            slot="activator"
            v-model="date"
            label="Delivery Date"
            prepend-icon="event"
            readonly
          ></v-text-field>
          <v-date-picker v-model="date" v-on:input="menu = onDateChanged(date)"></v-date-picker>
        </v-menu>
    </v-container>
</template>

<script>
import store from '../store';
import { SET_DELIVERY_LOCATION, SET_ORDER_DATE } from '../store/orders/mutation';

    export default {
        name: "OrderSettings",
        store,
        computed: {
            orderDate() {
                return this.$store.getters.getOrderDate;
            },
            storeNames() {
                return this.$store.getters.getStoreNames;
            },
            orderLocation() {
                return this.$store.getters.getDeliveryLocation;
            }
        },
        methods: {
                onDateChanged: function(date) {
                    this.$store.dispatch(SET_ORDER_DATE, date);
                    this.$store.dispatch(SET_ORDER_DATE, date);
                    return false;
                },
                onStoreNameChanged: function(location) {
                    this.$store.dispatch(SET_DELIVERY_LOCATION, location);
                }
        },
        data: () => ({
            routeRep: 'test',
            date: new Date().toISOString().substr(0, 10),
            menu: false,
        })
    }

</script>

<style scoped>

</style>
