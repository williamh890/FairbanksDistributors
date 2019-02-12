<template>
  <v-container class="size" fluid grid-list-xl>
    <h1>Create Order</h1>
    <v-select
      :items="types"
      v-on:change="onTypeChanged"
      label="Chip Type"
      ></v-select>

      <v-list v-if="!!type" two-line>
        <template v-for="item in selectedItems">
          <v-list-tile
            :key="item.name"
            avatar
          >
          <v-list-tile-avatar>

            <v-select :items="numbers"></v-select>

              </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title>
                {{ item.name }}
              </v-list-tile-title>
              <v-list-tile-sub-title>
                <b>upc:</b> {{ item.upc }}, <b>oz:</b> {{ item.oz }}, <b>case:</b> {{ item.case }}

              </v-list-tile-sub-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>
      </v-list>

    <v-btn
      block
      color="secondary"
      style="margin-top: 10px"
      v-on:click="$emit('submit-order')"
    >
      Submit Order
    </v-btn>
  </v-container>
</template>

<script>
import store from '../store';
import { SET_SELECTED_ITEM_TYPE } from '../store/orders/mutation';

export default {
  name: 'Order',
  store,
  computed: {
    selectedItems() {
      return this.$store.getters.getSelectedItems;
    },
    types() {
      return this.$store.getters.getItemTypes;
    },
    type() {
      return this.$store.getters.getSelectedType;
    }
  },
  methods:  {
    onTypeChanged: function(type) {
      this.$store.dispatch(SET_SELECTED_ITEM_TYPE, type);
    }
  },
  data: () => ({
    numbers: [0,1,2,3,4,5,6,7,8,9,10],
  })
}
</script>

<style>
.size {
  max-width: 100%;
  width: 600px;
}
</style>
