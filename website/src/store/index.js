import actions from './orders/actions';
import { mutations } from './orders/mutation';
import { getters } from './orders/getters';

import Vuex from 'vuex';

export default new Vuex.Store({
  strict: true,
  state: {
    isLoggedIn: false,
    items: []
  },
  actions,
  mutations,
  getters,
});
