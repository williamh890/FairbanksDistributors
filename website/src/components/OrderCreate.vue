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
            v-on:click="onOpenDialog(item)"
            avatar
          >

            <v-list-tile-content>
              <v-list-tile-title>
                {{ item.name }}
              </v-list-tile-title>
              <v-list-tile-sub-title>
                <b>upc:</b> {{ item.upc }}, <b>oz:</b> {{ item.oz }}, <b>case:</b> {{ item.case }}

              </v-list-tile-sub-title>
            </v-list-tile-content>

          <v-list-tile-action>
             <v-chip color="secondary" text-color="white">
               {{ item.amount }}
             </v-chip>
          </v-list-tile-action>
          </v-list-tile>
        </template>
      </v-list>

  <v-dialog v-model="dialog" max-width="290">
      <v-card>
        <v-card-title>
          {{ currentItem ? currentItem.name : '' }}
        </v-card-title>

            <v-text-field
              style="margin: 10px;"
              label="Amount"
              v-model="itemAmount"
              type="number"
              required
          ></v-text-field>

      <v-list>
          <v-list-tile
            v-for="(number, i) in numbers"
            :key="i"
            avatar
            v-on:click="onAmountClicked(number)"
          >
            <v-list-tile-content>
              <v-list-tile-title>{{ number }} </v-list-tile-title>
            </v-list-tile-content>

            <v-list-tile-avatar>
                <v-icon v-if="number === itemAmount">done</v-icon>
            </v-list-tile-avatar>

          </v-list-tile>
        </v-list>

        <v-card-actions>
          <v-btn
            block
            color="primary"
            v-on:click="onAddItem"
          >
            Add To Order
          </v-btn>
        </v-card-actions>

      </v-card>

    </v-dialog>
  </v-container>
</template>

<script>
import store from '../store';
import { SET_SELECTED_ITEM_TYPE, ADD_ORDER_ITEM } from '../store/orders/mutation';

export default {
  name: 'OrderCreate',
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
    },
    orderItems() {
      return this.$store.getters.orderItems;
    }
  },
  methods:  {
    onTypeChanged: function(type) {
      this.$store.dispatch(SET_SELECTED_ITEM_TYPE, type);
    },
    onOpenDialog: function(item) {
      this.dialog = true;
      this.itemAmount = 1;
      this.currentItem = item;
    },
    onAmountClicked: function(amount) {
      this.itemAmount = amount;
    },
    onAddItem: function() {
      this.$store.dispatch(ADD_ORDER_ITEM, {
        item: this.currentItem, amount: this.itemAmount
      });

      this.itemAmount = 1;
      this.currentItem = null;
      this.dialog = false;
    },
    amountInOrder: function(item, items) {

      const amount = (items.length === 0) ?
        0 : items
          .filter(i => i !== item)
          .map(i => i.amount)
          .pop();

      return amount;
    }
  },
  data: () => ({
    numbers: [1,2,3,4,5,6],
    dialog: false,
    currentItem: null,
    itemAmount: 1,
  })
}
</script>

<style>
.size {
  max-width: 100%;
  width: 600px;
}
</style>
