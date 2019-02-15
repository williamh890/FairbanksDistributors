<template>
    <v-container>
        <h1> Order Settings </h1>
        <v-menu
          ref="menu"
          v-model="menu"
          :close-on-content-click="true"
          :nudge-right="40"
          :return-value.sync="date"
          lazy
          transition="scale-transition"
          offset-y
          full-width
          min-width="290px"
        >
            <v-text-field
            slot="activator"
            v-model="date"
            label="Order Delivery Date"
            readonly
          ></v-text-field>
            <v-date-picker v-model="date" no-title scrollable @input="menu = false">
                <v-spacer></v-spacer>
                <v-btn flat color="primary" @click="menu = false">Cancel</v-btn>
                <v-btn flat color="primary" @click="menu = onDateChanged(date)">OK</v-btn>
            </v-date-picker>
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
            routeRep() {
                return this.$store.getters.getRouteRep;
            },
            orderDate() {
                return this.$store.getters.getOrderDate;
            },
        },
        methods: {
                onDateChanged: function(date) {
                    this.$store.dispatch(SET_ORDER_DATE, date);
                    return false;
                },
                onLocationChanged: function(location) {
                    this.$store.dispatch(SET_DELIVERY_LOCATION, location);
                }
        },
        data: () => ({
            routeRep: 'test',
            date: new Date().toISOString().substr(0, 10),
        })
    }

</script>

<style scoped>

</style>