<template>
  <v-container class="size" fluid grid-list-xl>
    <h1>Create Order</h1>
    <v-select
      :items="Object.keys(chips)"
      v-model="type"
      label="Chip Type"
      ></v-select>

      <v-list v-if="!!type" two-line>
        <template v-for="item in chips[type]">
          <v-list-tile
            :key="item.name"
            avatar
          >
          <v-list-tile-avatar>

            <v-select :items="numbers"></v-select>

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

    <v-btn
      block
      color="secondary"
      style="margin-top: 10px"
      v-on:click="$emit('submit-order')"
    >
      Submit Order
    </v-btn>
  </v-container>
</template>

<script>

export default {
  name: 'Order',
  data: () => ({
    numbers: [0,1,2,3,4,5,6,7,8,9,10],
    type: null,
    chips: {
      'Doritors': [{
      "name": "DORITOS COOL RANCH",
      "oz": 10.00,
      "upc": "FL-64132",
      "case": 7
    }, {
      "name": "DORITOS NACHO CHEESE",
      "oz": 10.00,
      "upc": "FL-64203",
      "case": 7
    }, {
      "name": "DORITOS TACO",
      "oz": 10.00,
      "upc": "FL-64191",
      "case": 7
    }, {
      "name": "DORITOS SPICY NACHO",
      "oz": 10.00,
      "upc": "FL-64204",
      "case": 7
    }, {
      "name": "DORITOS SPICY SWEET CHILI",
      "oz": 10.00,
      "upc": "FL-64225",
      "case": 7
    }, {
      "name": "DORITOS TAPATIO",
      "oz": 10.00	,
      "upc": "FL-64205"	,
      "case": 7
    }, {
      "name": "DORITOS JACKED RANCH HOT WINGS",
      "oz": 9.50,
      "upc": "FL-64226",
      "case": 7
    }, {
      "name": "DORITOS POPPIN\" JALAPEÑO",
      "oz": 9.75	,
      "upc": "FL-66655",
      "case": 7
    }, {
      "name": "DORITOS DINAMITA CHILE LIMÓN",
      "oz": 11.25	,
      "upc": "FL-65555",
      "case": 8
    }, {
      "name": "DORITOS BLAZE",
      "oz": 9.75	,
      "upc": "FL-92334",
      "case": 7
    }, {
      "name": "DORITOS FLAMIN' HOT NACHOS",
      "oz": 9.75,
      "upc": "FL-19924",
      "case": 7
    }
      ],
      'Cheetos': [{
    "name": "CHEETOS JUMBO PUFFS",
    "oz":8.00,
    "upc":"FL-59668",
    "case":10
  }, {
    "name": "CHEETOS CRUNCHY",
    "oz":8.50,
    "upc":"FL-58986",
    "case":8
  }, {
    "name": "CHEETOS CHED. JALAPENO",
    "oz":	8.50,
    "upc": "FL-58988",
    "case": 8
  }, {
    "name": "CHEETOS FLAMIN' HOT CRUNCHY",
    "oz":	8.50,
    "upc":"FL-58989",
    "case": 8
  }, {
    "name": "CHEETOS PAWS",
    "oz":	7.50,
    "upc": "FL-63801",
    "case":12
  }
      ],
      'Fritos': [{
      "name":"FS LAYS REGULAR",
      "oz":"10.25",
      "upc":"FL-64549",
      "case":"9"
   },
   {
      "name":"FS LAYS BBQ",
      "oz":"9.75",
      "upc":"FL-64524",
      "case":"10"
   },
   {
      "name":"FS LAYS SOUR CREAM & ONION",
      "oz":"9.75",
      "upc":"FL-64641",
      "case":"10"
   },
   {
      "name":"FS WAVY LAYS",
      "oz":"9.50",
      "upc":"FL-04389",
      "case":"11"
   },
   {
      "name":"FS LIGHTLY SALTED LAYS",
      "oz":"9.50",
      "upc":"FL-64644",
      "case":"10"
   }
      ]
    }
  })
}
</script>

<style>
.size {
  max-width: 100%;
  width: 600px;
}
</style>
