<template>
    <v-container>
        <h1> Order Settings </h1>
        <v-divider></v-divider>
        <v-menu
          v-model="menu"
          :close-on-content-click="true"
          :nudge-right="-10"
          lazy
          transition="scale-transition"
          offset-y
          full-width
          min-width="290px"
        >
          <v-text-field
            slot="activator"
            v-model=orderDate
            label="Delivery Date"
            append-icon="event"
            readonly
          ></v-text-field>
          <v-date-picker v-model="date" v-on:input="menu = onDateChanged(date)"></v-date-picker>
        </v-menu>
        <p class="subheading">Delivery Location</p>
        <v-radio-group @change="onStoreNameChanged">
            <template v-for="location in storeNames">
                <v-radio :label="location" :value="location"></v-radio>
            </template>
        </v-radio-group>
        <v-select class='pb-4' disabled label="Order Type" v-on:change="onOrderTypeChanged" :items="orderTypes"
                  hint="More order types coming soon!" persistent-hint placeholder="Chips">
                    <!--Remove the pb-4 when you remove the hint-->
        </v-select>
    </v-container>
</template>

<script>
import store from '../store';
import { SET_DELIVERY_LOCATION, SET_ORDER_DATE, SET_ORDER_TYPE } from '../store/orders/mutation';

function alaskaTime(){
    var offset = new Date().getTimezoneOffset()/60.0;
    return new Date(new Date().getTime() + 3600000*(-offset));
}

function nextDay(date){
    return new Date(date.getTime() + 86400000);
}

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
            orderTypes() {
                return this.$store.getters.getOrderTypes;
            },
            orderLocation() {
                return this.$store.getters.getDeliveryLocation;
            }
        },
        methods: {
                onDateChanged: function(date) {
                    this.$store.dispatch(SET_ORDER_DATE, date);
                    return false;
                },
                onStoreNameChanged: function(location) {
                    this.$store.dispatch(SET_DELIVERY_LOCATION, location);
                },
                onOrderTypeChanged: function(type) {
                    this.$store.dispatch(SET_ORDER_TYPE, type);
                }
        },
        data: () => ({
            routeRep: 'test',
            date: new nextDay(alaskaTime()).toISOString().substr(0, 10),
            menu: false,
            location: null,
        })
    }

</script>

<style scoped>

</style>
