<template>
  <v-container class="size" fluid grid-list-xl>
    <h1>Create Order</h1>
    <v-toolbar app v-show="showScrollSelector">
      <v-spacer></v-spacer>
      <v-select
        single-line
        :items="types"
        v-on:input="onTypeChanged"
        label="Select Item Category"
        ></v-select>
      <v-spacer></v-spacer>
    </v-toolbar>
      <v-select
        :items="types"
        v-on:input="onTypeChanged"
        label="Select Item Category"
        ></v-select>
      <v-list two-line subheader>
        <template v-for="item in allItems">
            <v-list-tile
              :key="item.name"
              :id="item.name"
              v-on:click="onOpenDialog(item)"
              avatar
            >

              <v-list-tile-content>
                <v-list-tile-title class="title">
                  {{ item.name }}
                </v-list-tile-title>
                <v-list-tile-sub-title>
                  <b>upc:</b> {{ item.upc }}, <b>oz:</b> {{ item.oz }}, <b>case:</b> {{ item.case }}

                </v-list-tile-sub-title>
              </v-list-tile-content>

              <v-list-tile-action class="hidden-xs-only">
                <v-btn icon>
                  <v-icon>remove</v-icon>
                </v-btn>
              </v-list-tile-action>
              <v-list-tile-action>
                 <v-chip color="secondary" text-color="white">
                   {{ item.amount }}
                 </v-chip>
              </v-list-tile-action>
              <v-list-tile-action class="hidden-xs-only">
                <v-btn icon>
                  <v-icon>add</v-icon>
                </v-btn>
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
    },
    allItems() {
      return this.$store.getters.getItems;
    },
  },
  methods:  {
    onTypeChanged: function(type) {
      this.$store.dispatch(SET_SELECTED_ITEM_TYPE, type);
      this.scrollPage(this.selectedItems[0].name);
      window.scrollBy(0, -60);
    },
      scrollPage: function(index) {
          document.getElementById(index).scrollIntoView();
    },
    setStick: function(value) {
      this.showScrollSelector = value;
    },
    onOpenDialog: function(item) {
      this.dialog = true;
      this.itemAmount = 1;
      this.currentItem = item;
    },
    onAmountClicked: function(amount) {
      this.itemAmount = amount;
      this.dialog = false;
      this.onAddItem()
    },
    onAddItem: function() {
      this.$store.dispatch(ADD_ORDER_ITEM, {
        item: this.currentItem, amount: parseInt(this.itemAmount)
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
    },
  },
  mounted() {
    window.addEventListener('scroll', () => {
      this.showScrollSelector = (Math.round(window.scrollY) > 175);
      this.setStick(window.scrollY>220);
    });
  },
  data: () => ({
    numbers: [1,2,3,4,5,6],
    dialog: false,
    currentItem: null,
    itemAmount: 1,
    showScrollSelector: false,
  })
}
</script>

<style>
.size {
  max-width: 100%;
  width: 600px;
}
</style>
