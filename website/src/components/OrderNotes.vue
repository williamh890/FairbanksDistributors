<template>
  <v-container>
    <h1>Order Notes</h1>
      <v-textarea v-model="orderNotes">Give me input</v-textarea>
  </v-container>
</template>
<script>
import store from '../store';

export default {
  name: 'Notes',
  store,
    data: () => ({
    orderNotes: '',
  })
}

</script>

<style>
</style>