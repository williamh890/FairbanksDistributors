import {
  LOGIN,
  LOGOUT,
  ADD_ORDER_ITEM ,
  CLEAR_ORDER_ITEMS,
  SUBMIT_ORDER
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

  clearOrderItem({ commit }) {
    commit(CLEAR_ORDER_ITEMS);
  },

  submitOrder({ commit }) {
    commit(SUBMIT_ORDER);
  }
};
