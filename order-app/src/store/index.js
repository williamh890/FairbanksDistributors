import actions from './orders/actions';
import { mutations } from './orders/mutation';

import Vuex from 'vuex';

export default new Vuex.Store({
  strict: true,
  state: {
    todos: []
  },
  actions,
  mutations
});
