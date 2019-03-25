import { chips, chipTypes } from '../chips';

export const LOGIN = 'login';
export const LOGOUT = 'logout';
export const SHOWMAIN = 'showMain';
export const HIDEMAIN = 'hideMain';

export const SET_SELECTED_ITEM_TYPE = 'setSelectedItemType';

export const ADD_ORDER_ITEM = 'addOrderItem';
export const CLEAR_ORDER_ITEMS = 'clearOrderItems';
export const CLEAR_ORDER_SETTINGS = 'clearOrderSettings';

export const SUBMIT_ORDER = 'submitOrder';

export const SET_DELIVERY_LOCATION = 'setDeliveryLocation';
export const SET_ORDER_DATE = 'setOrderDate';
export const SET_ORDER_TYPE = 'setOrderType';

export const ADD_ORDER_NOTES = 'addOrderNotes';

export const mutations = {
  [LOGIN]: function(state) {
    state.isLoggedIn = true;
    state.mainMenu = true;
  },

  [LOGOUT]: function(state) {
    state.isLoggedIn = false;
  },

  [SHOWMAIN]: function(state) {
    state.mainMenu = true;
  },

  [HIDEMAIN]: function(state) {
    state.mainMenu = false;
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
    state.order.items = [];
    state.items = chips.map(item => {
      item.amount = 0;
      return item;
    });
    state.selectedType = null;
  },

  [CLEAR_ORDER_SETTINGS]: function(state) {
    state.order.deliveryLocation = null;
  },

  [SUBMIT_ORDER]: function(state) {
    state.submit = true;
  },

  [SET_DELIVERY_LOCATION]: function(state, storeName) {
    state.order.deliveryLocation = storeName;
  },

  [SET_ORDER_DATE]: function(state, date) {
    state.order.date = date;
  },

  [SET_ORDER_TYPE]: function(state, type) {
    state.order.type = type;
    if (type === 'Chips') {
      state.itemTypes = chipTypes;
      state.items = chips.map(item => {
      item.amount = 0;
      return item
      })
    }
    else {
      state.itemTypes = [];
      state.items = null;
    }
  },

  [ADD_ORDER_NOTES]: function(state, notes) {
    state.order.orderNotes = notes;
  }
};
