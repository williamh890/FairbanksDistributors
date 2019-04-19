import {
  LOGIN,
  LOGOUT,
  ADD_ORDER_ITEM,
  CLEAR_ORDER_ITEMS,
  CLEAR_ORDER_SETTINGS,
  SUBMIT_ORDER,
  SET_SELECTED_ITEM_TYPE,
  SET_ORDER_DATE,
  SET_DELIVERY_LOCATION,
  SET_CATEGORIES,
  HIDEMAIN,
  SHOWMAIN,
  ADD_ORDER_NOTES, SET_ORDER_TYPE,
} from './mutation';

export default {
  login({ commit }, password) {
    commit(LOGIN, password);
  },

  logout({ commit }) {
    commit(LOGOUT);
  },

  hideMain({ commit }) {
    commit(HIDEMAIN);
  },

  setCategories({ commit }, categories) {
    commit(SET_CATEGORIES, categories);
  },

  showMain({ commit }) {
    commit(SHOWMAIN);
  },

  addOrderItem({ commit }, item) {
    commit(ADD_ORDER_ITEM, item);
  },

  setSelectedItemType({ commit }, type) {
    commit(SET_SELECTED_ITEM_TYPE, type);
  },

  clearOrderItems({ commit }) {
    commit(CLEAR_ORDER_ITEMS);
  },

  clearOrderSettings({ commit }) {
    commit(CLEAR_ORDER_SETTINGS);
  },

  submitOrder({ commit }) {
    commit(SUBMIT_ORDER);
  },

  setOrderDate({ commit }, date) {
    commit(SET_ORDER_DATE, date);
  },

  setOrderType({ commit }, type) {
    commit(SET_ORDER_TYPE, type);
  },

  setDeliveryLocation({ commit}, location) {
    commit(SET_DELIVERY_LOCATION, location);
  },

  addOrderNotes({ commit }, notes) {
    commit(ADD_ORDER_NOTES, notes);
  }

};
