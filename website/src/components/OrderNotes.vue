<template>
  <v-container>
    <h1>Order Notes</h1>
      <v-textarea v-model="orderNotes"
                  v-on:change="this.addNotes"
                  label="Add notes for the warehouse">
      </v-textarea>
  </v-container>
</template>
<script>
import store from '../store';
import { ADD_ORDER_NOTES } from '../store/orders/mutation';

export default {
  name: 'Notes',
  store,
    data: () => ({
    orderNotes: '',
  }),
    methods: {
      addNotes() {
          this.$store.dispatch(ADD_ORDER_NOTES, this.orderNotes);
          console.log(this.orderNotes);
      }
    }
}

</script>

<style>
</style>