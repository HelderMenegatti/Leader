<template>
    <v-container>
        <v-row class="flex-child text-subtitle-2">
            <v-col cols="4">
                <v-col
                class="d-flex"
                cols="12"
                
                >
                    <CarouselDatailProduct />
                </v-col>
            </v-col>
            <v-col cols="8" height="100" v-if="loading">
                <p>Carregando...</p>
            </v-col>
            <v-col cols="8" height="100" v-else-if="product">
                <DetailProductList />                          
            </v-col>
            <v-col cols="8" height="100" v-else>
                <p>Produto não encontrado</p>                       
            </v-col>
        </v-row>
    </v-container>
</template>
<script setup>

import { useRoute } from 'vue-router';
import {useProductDetailStore} from '@/stores/productDetail'

const productDetailStore = useProductDetailStore()
const route = useRoute();

productDetailStore.getDetailProduct(route.query.pk)

const product = computed(() => productDetailStore.product);
const loading = computed(() => productDetailStore.loading);


onMounted(() => {
    const productId = route.query.pk;
    if (productId) {
      productDetailStore.getDetailProduct(productId);
    }
});


</script>