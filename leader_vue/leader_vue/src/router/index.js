/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
import { createRouter, createWebHistory } from 'vue-router/auto'
import { setupLayouts } from 'virtual:generated-layouts'
import Products from '@/pages/Products.vue'
import ListProducts from '@/pages/ListProducts.vue'
import DefaultLayout from '@/layouts/default.vue'

const routes = [
  {
    path: '/',
    component: DefaultLayout,
    children: [
      {
        path: '/',
        name: 'Products',
        component: Products,
      },
      {
        path: '/list-products',
        name: 'ListProducts',
        component: ListProducts,
      },
    ],
  },
]




const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  // extendRoutes: (routes) => setupLayouts(routes),
  extendRoutes: (routes) => [
    {
      path: '/',
      component: DefaultLayout,
      children: [
        {
          path: '/category-products',
          name: 'Products',
          component: Products,
        },
        {
          path: '/list-products',
          name: 'ListProducts',
          component: ListProducts,
        },
      ],
    },
  ],

  // routes,

})

export default router
