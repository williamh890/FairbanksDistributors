export const LOGIN = 'login';
export const LOGOUT = 'logout';

export const SET_SELECTED_ITEM_TYPE = 'setSelectedItemType';

export const ADD_ITEM = 'updateItemAmount';
export const CLEAR_ORDER_ITEMS = 'clearOrderItems';

export const SUBMIT_ORDER = 'submitOrder';

export const mutations = {
  [LOGIN]: function(state) {
    state.isLoggedIn = true;
  },

  [LOGOUT]: function(state) {
    state.isLoggedIn = false;
  },

  [ADD_ITEM]: function(state, item, amount) {
  },

  [SET_SELECTED_ITEM_TYPE]: function(state, type) {
    state.selectedType = type;
  },

  [CLEAR_ORDER_ITEMS]: function(state) {
    state.items = [];
  },

  [SUBMIT_ORDER]: function(state) {
    state.submit = true;
  }
};
