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

export default {
  name: 'Notes',
  store,
    data: () => ({
    orderNotes: '',
  }),
    methods: {
      addNotes() {
          console.log(this.orderNotes);
      }
    }
}

</script>

<style>
</style>