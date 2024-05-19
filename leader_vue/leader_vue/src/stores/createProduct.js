import { defineStore } from 'pinia';
import { ref } from 'vue';
import axios from 'axios';
import { useProductStore } from '@/stores/products'


export const useCreateProductStore = defineStore('CreateProduct', {
    state: () => ({
        dialog: ref(false)
    }),
    actions: {
        addProduct(productData) {
            axios.post('http://127.0.0.1:8000/api/products/', productData, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                const productsStore = useProductStore();
                productsStore.products.value.push(response.data)
                this.dialog = false;

            })
            .catch(error => {
                console.error("Erro ao enviar dados:", error);
            });
        }
    }
});
