<template>
  <v-app id="inspire">
    <v-system-bar>
      <v-spacer></v-spacer>

      <v-icon>mdi-square</v-icon>

      <v-icon>mdi-circle</v-icon>

      <v-icon>mdi-triangle</v-icon>
    </v-system-bar>

    <v-app-bar>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-app-bar-title>Leader</v-app-bar-title>

      <template v-slot:append>
        
        <v-btn icon="mdi-magnify"></v-btn>
        
        <v-btn icon="mdi-heart"></v-btn>

        <v-btn icon="mdi-cart-outline"></v-btn>

        <v-btn icon="mdi-account"></v-btn>
        
        <v-btn icon="mdi-dots-vertical"></v-btn>
      </template>

    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      temporary
    >
      <!--  -->
    </v-navigation-drawer>

    <v-main class="bg-grey-lighten-2">

      <!-- <v-container>
        <v-row>
          <template v-for="n in 4" :key="n">
            <v-col
              class="mt-2"
              cols="12"
            >
              <strong>Category {{ n }}</strong>
            </v-col>

            <v-col
              v-for="j in 6"
              :key="`${n}${j}`"
              cols="6"
              md="2"
            >
              <v-sheet height="150"></v-sheet>
            </v-col>
          </template>
        </v-row>
      </v-container> -->
      <div class="defalt-size-project-body">

        <router-view></router-view>
      </div>
    </v-main>
  </v-app>
</template>

<script setup>
  import { ref } from 'vue'

  const drawer = ref(null)
</script>

<script>
  export default {
    data: () => ({ drawer: null }),
  }
</script>

<style scoped>
.defalt-size-project-body{
  margin-top: 2%;
  margin-left: 4%;
  margin-right: 4%;
}
</style>