export const LOGIN = 'login';
export const LOGOUT = 'logout';

export const ADD_ORDER_ITEM = 'addOrderItem';
export const CLEAR_ORDER_ITEMS = 'clearOrderItems';

export const SUBMIT_ORDER = 'submitOrder';

export const mutations = {
  [LOGIN]: function(state) {
    state.login = true;
  },

  [LOGOUT]: function(state) {
    state.logout = false;
  },

  [ADD_ORDER_ITEM]: function(state, item) {
    state.items = [...state.items, item];
  },

  [CLEAR_ORDER_ITEMS]: function(state) {
    state.items = [];
  },

  [SUBMIT_ORDER]: function(state) {
    state.submit = true;
  }
};
