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
"items":[{"item":{"type":"Doritos","name":"DORITOS COOL RANCH","oz":10,"upc":"FL-64132","case":7,"amount":3},"amount":3},{"item":{"type":"Doritos","name":"DORITOS NACHO CHEESE","oz":10,"upc":"FL-64203","case":7,"amount":3},"amount":3}]    },
  },
  actions,
  mutations,
  getters,
});
