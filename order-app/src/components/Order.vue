<template>
  <v-container class="size" fluid grid-list-xl>
    <h1>Chip Order</h1>
    <v-select
      :items="chipTypes"
      label="Chip Type"
      ></v-select>

      <v-list two-line>
        <template v-for="(item, index) in chips">
          <v-list-tile
            :key="item.name"
            avatar
            @click=""
          >
          <v-list-tile-avatar>

            <v-select
              :items="numbers"
              ></v-select>

              </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title>
                {{ item.name }}
              </v-list-tile-title>
              <v-list-tile-sub-title>
                <b>upc:</b> {{ item.upc }}, <b>oz:</b> {{ item.oz }}, <b>case:</b> {{ item.case }}

              </v-list-tile-sub-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>
      </v-list>
      </div>
  </v-container>
</template>

<script>

export default {
  name: 'Order',
  data: () => ({
    chipTypes: [
      'Doritos', 'Cheetos', 'Fritos', 'Family Size Lays',
      'XL Lays', 'Ruffles', 'Misc Chips', 'Party Size',
      'Tube Snack Nuts', 'Matador Jerky', "Grandma's Big Cookies",
      'Display Supplies', 'Ready To Go', 'In and Out',
      'Dips/Salsa', 'Extra Extra Large Value Line (XXVL)',
      'Baked - Reduced Fat', 'Naturals - Organic',' Sunchips',
      'Rold Gold', 'Kettle Cooked', 'Variety Packs', 'Tostitos',
      'Santitas'
    ],
    numbers: [1,2,3,4,5,6,7,8,9,10],
    chips:
 [{
  name: "DORITOS COOL RANCH",
  oz: 10.00,
  upc: "FL-64132",
  case: 7
}, {
  name: "DORITOS NACHO CHEESE",
  oz: 10.00,
  upc: "FL-64203",
  case: 7
}, {
  name: "DORITOS TACO",
  oz: 10.00,
  upc: "FL-64191",
  case: 7
}, {
  name: "DORITOS SPICY NACHO",
  oz: 10.00,
  upc: "FL-64204",
  case: 7
}, {
  name: "DORITOS SPICY SWEET CHILI",
  oz: 10.00	,upc: "FL-64225",	case: 7
}, {
  name: "DORITOS TAPATIO",
  oz: 10.00	,
  upc: "FL-64205"	,
  case: 7
}, {
  name: "DORITOS JACKED RANCH HOT WINGS",
  oz: 9.50,
  upc: "FL-64226",
  case: 7
}, {
  name: "DORITOS POPPIN\" JALAPEÑO",
  oz: 9.75	,
  upc: "FL-66655",
  case: 7
}, {
  name: "DORITOS DINAMITA CHILE LIMÓN",
  oz: 11.25	,
  upc: "FL-65555",
  case: 8
}, {
  name: "DORITOS BLAZE",
  oz: 9.75	,
  upc: "FL-92334",
  case: 7
}, {
  name: "DORITOS FLAMIN\' HOT NACHOS",
  oz: 9.75,
  upc: "FL-19924",
  case: 7
}
]
})
}
</script>

<style>
.size {
  max-width: 100%;
  width: 800px;
}
</style>
