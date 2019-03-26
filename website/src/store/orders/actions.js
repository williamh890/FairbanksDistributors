import {
  LOGIN,
  LOGOUT,
  ADD_ORDER_ITEM,
  CLEAR_ORDER_ITEMS,
  SUBMIT_ORDER,
  SET_SELECTED_ITEM_TYPE,
  SET_ORDER_DATE,
  SET_DELIVERY_LOCATION,
  HIDEMAIN,
  SHOWMAIN,
  ADD_ORDER_NOTES,
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

  submitOrder({ commit }) {
    commit(SUBMIT_ORDER);
  },

  setOrderDate({ commit }, date) {
    commit(SET_ORDER_DATE, date);
  },

  setDeliveryLocation({ commit}, location) {
    commit(SET_DELIVERY_LOCATION, location);
  },

  addOrderNotes({ commit }, notes) {
    commit(ADD_ORDER_NOTES, notes);
  }

};
