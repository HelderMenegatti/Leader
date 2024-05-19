<template>
  <v-container>
    <v-row>
      <v-col cols="12" class="d-flex justify-end">
        <CreateProduct />
      </v-col>
      <v-col cols="12">
        <TableDataDisplay />
      </v-col>
    </v-row>
  </v-container>
  
</template>

<script setup>
  import { useProductStore } from '@/stores/products'

  const productsStore = useProductStore();

  productsStore.getProducts()
</script>

<style>

</style>