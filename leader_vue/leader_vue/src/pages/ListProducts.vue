<template>
  <div>

    <TableDataDisplay />
  </div>
</template>

<script setup>
  import { useProductStore } from '@/stores/products'

  import { onMounted, ref } from 'vue';

  const productsStore = useProductStore();

  onMounted(()=>{
    productsStore.getProducts()
  })
  
</script>

<style>

</style>