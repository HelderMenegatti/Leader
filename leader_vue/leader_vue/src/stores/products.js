import { defineStore } from 'pinia';
import { ref } from 'vue';

import axios from 'axios';


export const useProductStore = defineStore('product', {
    state: () => ({
        products: ref([]),
        loaded: false
    }),
    actions:{
        async getProducts(){
            await axios.get('http://127.0.0.1:8000/api/products/').then(response=> {
                this.products.value = response.data;
                if(this.products.value){

                    this.loaded = true
                }
            }).catch(error=> {
                console.error("Erro ao buscar dados:", error)
            })
        }
    }
})
