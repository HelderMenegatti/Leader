<template>
  <v-card flat>
    <v-card-title class="d-flex align-center pe-2">
      <v-icon icon="mdi-video-input-component"></v-icon> &nbsp;
      Lista de Produtos

      <v-spacer></v-spacer>

      <v-text-field
        v-model="search"
        density="compact"
        label="Search"
        prepend-inner-icon="mdi-magnify"
        variant="solo-filled"
        flat
        hide-details
        single-line
      ></v-text-field>
    </v-card-title>

    <v-divider></v-divider>

    <v-data-table v-model:search="search" :headers="headers" :items="items">
      <template v-slot:header.stock>
        <div class="text-end">Stock</div>
      </template>

      <template v-slot:item.product_code="{ item }">
        <div class="text-start">
          <v-btn 
            variant="text" color="primary" 
            :href="'/detail-product?pk=' + item.id" 
            target="_blank"
          >
          
            {{ item.product_code }}
          </v-btn>
        </div>
      </template>

      <template v-slot:item.stock="{ item }">
        <div class="text-end">
          <v-chip
            :color="item.stock ? 'green' : 'red'"
            :text="item.stock ? 'In stock' : 'Out of stock'"
            class="text-uppercase"
            size="small"
            label
          ></v-chip>
        </div>
      </template>
    </v-data-table>

  </v-card>
</template>

  <script setup>

  import { useProductStore } from '@/stores/products'
  import { ref, computed } from 'vue';


  const productsStore = useProductStore();
  
  const headers = [
    { title: 'ID', key: 'id' },
    { title: 'Código do produto', key: 'product_code' },
    { title: 'Nome', key: 'name' },
    { title: 'Medida unitária', key: 'get_unit_measurement_display' },
    { title: 'Preço', key: 'price' },
    { title: 'Stock', key: 'stock' }
  ];

  const items = computed(()=> productsStore.products.value);

  const search = ref('');
  </script>