import actions from './orders/actions';
import { mutations } from './orders/mutation';
import { getters } from './orders/getters';
import { storeNames } from './routes';
import Vuex from 'vuex';

export default new Vuex.Store({
  strict: true,
  state: {
    password: null,
    isLoggedIn: false,
    mainMenu: false,
    items: [],
    itemTypes: [],
    selectedType: null,
    order: {
      items:[],
      date: new Date().toISOString().substr(0, 10),
      deliveryLocation: null,
      orderNotes: '',
    },
    storeNames: storeNames,
  },
  actions,
  mutations,
  getters,
});
