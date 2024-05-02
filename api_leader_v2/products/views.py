from rest_framework import viewsets

from products.models import Product, Cart, CartItem
from products.serializers import ProductSerializer, CartSerializer, CartItemSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(viewsets.ModelViewSet):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewset(viewsets.ModelViewSet):

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
