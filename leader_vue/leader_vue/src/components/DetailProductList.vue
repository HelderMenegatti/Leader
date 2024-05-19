<template>
  <v-card 
    class="mx-auto" 
    :title="product.name" 
    :subtitle="product.product_code" 
    width="98%"
  >

    <template v-slot:append>
      <v-container>

        <v-row align="center" justify="center">
          <v-col cols="auto">
            <v-btn density="compact" icon="mdi-pencil"></v-btn>
          </v-col>
          <v-col cols="auto">
            <v-btn density="compact" icon="mdi-delete"></v-btn>
          </v-col>  
        </v-row>
      </v-container>
    </template>


    <v-card-text class="bg-surface-light pt-4">
      <v-row>
        <v-col cols="2">
          <v-card title="Valor" :text="product.price"></v-card>
        </v-col>
        <v-col cols="3">
          <v-card title="Medida unitária" :text="product.get_unit_measurement_display"></v-card>
        </v-col>
        <v-col cols="3">
          <v-card title="Quantidade em stock" :text="product.stock ? 'Em estoque' : 'Sem estoque'"></v-card>
        </v-col>
        <v-col cols="12">
          <v-card title="Descrição" :text="product.description"></v-card>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>
  
  <script setup>
  import { computed } from 'vue';
  import { useProductDetailStore } from '@/stores/productDetail';

  const productDetailStore = useProductDetailStore();
  
  const product = computed(() => productDetailStore.product);
  
  </script>