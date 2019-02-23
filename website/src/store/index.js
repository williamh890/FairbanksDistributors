import actions from './orders/actions';
import { mutations } from './orders/mutation';
import { getters } from './orders/getters';
import { chips, chipTypes } from './chips';
import { routes, storeNames } from './routes';
import Vuex from 'vuex';

export default new Vuex.Store({
  strict: true,
  state: {
    isLoggedIn: false,
    mainMenu: false,
    items: chips.map(item => {
      item.amount = 0;
      return item
    }),
    itemTypes: chipTypes,
    selectedType: null,
    order: {
      items:[],
      date: new Date().toISOString().substr(0, 10),
      deliveryLocation: null
    },
    storeNames: storeNames,
  },
  actions,
  mutations,
  getters,
});
