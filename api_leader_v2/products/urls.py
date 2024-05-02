from django.urls import path, include

from rest_framework.routers import DefaultRouter

from products import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'cart', views.CartViewSet, basename='cart')
router.register(r'cart-items', views.CartItemViewset, basename='cart-items')


urlpatterns = [
    path('', include(router.urls)),
]

