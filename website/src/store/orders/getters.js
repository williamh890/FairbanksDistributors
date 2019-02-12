export const getters = {
  getIsLoggedIn: state => state.isLoggedIn,
  getItems: state => state.items,
  getItemTypes: state => state.itemTypes,
  getSelectedType: state => state.selectedType,
  getSelectedItems: state => state.items
    .filter(item => item.type === state.selectedType),
  getOrderItems: state => state.order.items
};
