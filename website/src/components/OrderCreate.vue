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
      <v-list subheader>
        <template v-for="category of allItems">
          <v-divider></v-divider>
          <v-toolbar :id="category.name" color="primary" class="headline" dark flat>
            {{ category.name}}
          </v-toolbar>
          <template v-for="item in category.items">
            <v-divider></v-divider>
            <v-list-tile
              v-on:click="onOpenDialog(item)"
            >

              <v-list-tile-content>
                <v-list-tile-title class="title">
                  {{ item.name.replace(category.name, '') }}
                </v-list-tile-title>
              </v-list-tile-content>

              <v-list-tile-action class="hidden-xs-only">
                <v-btn icon>
                  <v-icon>remove</v-icon>
                </v-btn>
              </v-list-tile-action>
              <v-list-tile-action>
                 <v-chip v-bind:color="item.amount !== 0 ? 'primary' : '' "
                         v-bind:dark="item.amount !== 0">
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
        </template>
      </v-list>

  <v-dialog v-model="dialog" max-width="290" transition="slide-fade" v-bind:hide-overlay="true">
      <v-card>
         <v-card-title v-if="currentItem">
            <div>
              <div>
                <h3>{{ currentItem.name }}</h3>
              </div>
              <span>
                upc: {{ currentItem.upc }},
                oz: {{ currentItem.oz }},
                case: {{ currentItem.case }}
              </span>
            </div>
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
            color="error"
            v-on:click="onCloseDialog"
          >
            Cancel
          </v-btn>
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
      return this.$store.getters.getCategories;
    },
  },
  methods:  {
    onTypeChanged: function(type) {
      this.$store.dispatch(SET_SELECTED_ITEM_TYPE, type);
      this.scrollPage(type);
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
      this.itemAmount = 0;
      this.currentItem = item;
    },
    onCloseDialog: function() {
      this.dialog = false;
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

      this.itemAmount = 0;
      this.currentItem = null;
      this.dialog = false;
    },
  },
  mounted() {
    window.addEventListener('scroll', () => {
      this.showScrollSelector = Math.round(window.scrollY) > 175;
      this.setStick(window.scrollY > 220);
    });
  },
  data: () => ({
    numbers: [0,1,2,3,4,5,6],
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
.slide-fade-enter-active {
  transition: all .05s ease;
}
.slide-fade-leave-active {
  transition: all .1s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateY(30px);
  opacity: 0;
}
</style>
