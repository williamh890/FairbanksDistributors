<template>
    <v-container>
        <h1> Order Settings </h1>
        <v-menu
          ref="menu"
          v-model="menu"
          :close-on-content-click="true"
          :nudge-right="40"
          :return-value.sync="date"
          lazy
          transition="scale-transition"
          offset-y
          full-width
          min-width="290px"
        >
            <v-date-picker v-model="date" no-title scrollable>
                <v-spacer></v-spacer>
                <v-btn flat color="primary" @click="menu = false">Cancel</v-btn>
                <v-btn flat color="primary" @click="$refs.menu.save(date)">OK</v-btn>
            </v-date-picker>
        </v-menu>
    </v-container>
</template>

<script>
    export default {
        name: "OrderSettings"
    }
</script>

<style scoped>

</style>