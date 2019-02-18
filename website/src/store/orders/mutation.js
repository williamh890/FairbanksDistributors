export const LOGIN = 'login';
export const LOGOUT = 'logout';

export const SET_SELECTED_ITEM_TYPE = 'setSelectedItemType';

export const ADD_ORDER_ITEM = 'addOrderItem';
export const CLEAR_ORDER_ITEMS = 'clearOrderItems';

export const SUBMIT_ORDER = 'submitOrder';

export const SET_DELIVERY_LOCATION = 'setDeliveryLocation';
export const SET_ORDER_DATE = 'setOrderDate';

export const mutations = {
  [LOGIN]: function(state) {
    state.isLoggedIn = true;
  },

  [LOGOUT]: function(state) {
    state.isLoggedIn = false;
  },

  [ADD_ORDER_ITEM]: function(state, orderItem) {
    state.order.items = [
      ...state.order.items, orderItem
    ];

    state.items
      .filter(item => item === orderItem.item)
      .forEach(item => item.amount = orderItem.amount)
  },

  [SET_SELECTED_ITEM_TYPE]: function(state, type) {
    state.selectedType = type;
  },

  [CLEAR_ORDER_ITEMS]: function(state) {
    state.items = [];
  },

  [SUBMIT_ORDER]: function(state) {
    state.submit = true;
  },

  [SET_DELIVERY_LOCATION]: function(state, storeName) {
    state.deliveryLocation = storeName;
  },

  [SET_ORDER_DATE]: function(state, date) {
    state.order.date = date;
  }
};
