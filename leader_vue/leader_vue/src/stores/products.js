import { defineStore } from 'pinia';
import { ref } from 'vue';

import axios from 'axios';


export const useProductStore = defineStore('product', {
    state: () => ({
        products: ref([]),
    }),
    actions:{
        getProducts(){
            axios.get('http://127.0.0.1:8000/api/products/').then(response=> {
                this.products.value = response.data;
            }).catch(error=> {
                console.error("Erro ao buscar dados:", error)
            })
        }
    }
})
