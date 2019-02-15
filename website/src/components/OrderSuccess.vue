<template>
  <v-container>
    <h1>Order Success!</h1>
    <h2> Delivery date: {{ orderDate }} </h2>
  </v-container>
</template>
<script>
import store from '../store';

export default {
  name: 'Success',
  store,
        computed: {
            orderDate() {
                return this.$store.getters.getOrderDate;
            }
        },
}

</script>

<style>
</style>
