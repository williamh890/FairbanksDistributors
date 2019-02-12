import actions from './orders/actions';
import { mutations } from './orders/mutation';
import { getters } from './orders/getters';
import { chips, chipTypes } from './chips';

import Vuex from 'vuex';

export default new Vuex.Store({
  strict: true,
  state: {
    isLoggedIn: true,
    items: chips.map(item => {
      item.amount = 0
      return item
    }),
    itemTypes: chipTypes,
    selectedType: "Doritos",
    order: {
      items: [],
    },
  },
  actions,
  mutations,
  getters,
});
