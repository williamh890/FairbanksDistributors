import {
  LOGIN,
  LOGOUT,
  ADD_ORDER_ITEM,
  CLEAR_ORDER_ITEMS,
  SUBMIT_ORDER,
  SET_SELECTED_ITEM_TYPE,
  SET_ORDER_DATE,
} from './mutation';

export default {
  login({ commit }) {
    commit(LOGIN);
  },

  logout({ commit }) {
    commit(LOGOUT);
  },

  addOrderItem({ commit }, item) {
    commit(ADD_ORDER_ITEM, item);
  },

  setSelectedItemType({ commit }, type) {
    commit(SET_SELECTED_ITEM_TYPE, type);
  },

  clearOrderItem({ commit }) {
    commit(CLEAR_ORDER_ITEMS);
  },

  submitOrder({ commit }) {
    commit(SUBMIT_ORDER);
  },

  setOrderDate({ commit }, date) {
    commit(SET_ORDER_DATE, date)
  }

};
