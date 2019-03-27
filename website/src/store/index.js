import actions from './orders/actions';
import { mutations } from './orders/mutation';
import { getters } from './orders/getters';
import { chips, chipTypes } from './chips';
import { routes, storeNames } from './routes';
import Vuex from 'vuex';

function alaskaTime(){
    var offset = new Date().getTimezoneOffset()/60.0;
    return new Date(new Date().getTime() + 3600000*(-offset));
}

function nextDay(date){
    return new Date(date.getTime() + 86400000);
}

export default new Vuex.Store({
  strict: true,
  state: {
    isLoggedIn: false,
    mainMenu: false,
    items: chips.map(item => {
      item.amount = 0;
      return item
    }),
    itemTypes: chipTypes,
    selectedType: null,
    order: {
      items:[],
      date: new nextDay(alaskaTime()).toISOString().substr(0, 10),
      deliveryLocation: null,
      orderNotes: '',
    },
    storeNames: storeNames,
  },
  actions,
  mutations,
  getters,
});
