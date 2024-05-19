import { defineStore } from 'pinia';
import { ref } from 'vue';
import axios from 'axios';

export const useProductDetailStore = defineStore('productDetail', {
  state: () => ({
    product: ref(null),
    loading: ref(false),
  }),
  actions: {
    async getDetailProduct(id) {
      this.loading = true;
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/products/${id}/`);
        this.product = response.data;
      } catch (error) {
        console.error("Erro ao buscar dados:", error);
      } finally {
        this.loading = false;
      }
    },
  },
});