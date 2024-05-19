<template>
 
    <div class="pa-4 text-center">
    <v-dialog
      v-model="createPruductStore.dialog"
      max-width="600"
    >
      <template v-slot:activator="{ props: activatorProps }">
        <v-btn
          class="text-none font-weight-regular"
          density="compact"
          icon="mdi-plus"
          v-bind="activatorProps"
        ></v-btn>
      </template>
  
      <v-card
        prepend-icon="mdi-plus"
        title="Cadastrer Produto"
      >
        <v-card-text>
          <v-row dense>
            <v-col
              cols="12"
              md="12"
              sm="6"
            >
              <v-text-field
                label="Nome do produto"
                required
                v-model="productData.name"
              ></v-text-field>
            </v-col>

            <v-col
              cols="12"
              md="6"
              sm="6"
            >
              <v-text-field
                label="Código do produto"
                v-model="productData.product_code"
              ></v-text-field>
            </v-col>


            <v-col
              cols="12"
              md="6"
              sm="6"
            >
              <v-text-field
                label="Preço"
                required
                v-model="productData.new_price"
                prefix="R$"
              ></v-text-field>
            </v-col>


            <v-col
              cols="12"
              sm="12"
            >
              <v-select
                :items="selectItems"
                label="mensutamento de unidades"
                required
                v-model="productData.unit_measurement"
              ></v-select>
            </v-col>


            <v-col
              cols="12"
              md="12"
              sm="12"
            >
                <v-textarea
                  :counter="300"
                  class="mb-2"
                  rows="2"
                  label="Descrição"
                  persistent-counter
                  v-model="productData.description"
                ></v-textarea>
            </v-col>
          </v-row>  
          <small class="text-caption text-medium-emphasis">*indicates required field</small>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            text="Close"
            variant="plain"
            @click="createPruductStore.dialog = false"
          ></v-btn>

          <v-btn
            color="primary"
            text="Save"
            variant="tonal"
            @click="createPruductStore.addProduct(productData)"
            ></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>

</template>

<script setup>
import { ref } from 'vue';
import { useCreateProductStore } from '@/stores/createProduct';


const selectItems = ref([
  { title: 'Unidades', value: 'unit' },
  { title: 'Quilos', value: 'kilo' },
  { title: 'Litros', value: 'liter' },

]);

const createPruductStore = useCreateProductStore();


var productData = ref({
  "product_code": "",
  "name": "",
  "description": "",
  "unit_measurement": "",
  "new_price": ""
});

</script>