export const getters = {
  getIsLoggedIn: state => state.isLoggedIn,
  getIsMainMenuActive: state => state.mainMenu,
  getItems: state => state.items,
  getItemTypes: state => state.itemTypes,
  getSelectedType: state => state.selectedType,
  getSelectedItems: state => state.items
    .filter(item => item.type === state.selectedType),
  getOrderItems: state => state.order.items.map(item => item.item),
  getRouteRep: state => state.routeRep,
  getOrderDate: state => state.order.date,
  getStoreNames: state => state.storeNames,
  getDeliveryLocation: state => state.order.deliveryLocation,
  getOrderNotes: state => state.order.orderNotes,
  getOrder: state => ({
    store: state.order.deliveryLocation,
    items: state.order.items.map(orderItem => {
        return {...orderItem.item};
      }),
    date: state.order.date,
  })
};
