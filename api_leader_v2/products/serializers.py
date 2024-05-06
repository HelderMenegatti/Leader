from rest_framework import serializers
from products.models import Product, PriceHistory, Cart, CartItem


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    new_price = serializers.DecimalField(max_digits=10, decimal_places=2, write_only=True)

    # image = serializers.SerializerMethodField()

    stock = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "product_code", 
            "name",
            # "description",
            "get_unit_measurement_display",
            "price",
            "new_price",
            "stock"
        ]


    def get_price(self, obj):
        return obj.price_history.first().price

    def get_stock(self, obj):
        return True


    def create(self, validated_data):
        new_price = validated_data.pop('new_price')
        product = Product.objects.create(**validated_data)
        PriceHistory.objects.create(product=product, price=new_price)
        return product


    def update(self, instance, validated_data):
        new_price = validated_data.pop('new_price')
        PriceHistory.objects.create(product=instance, price=new_price)
        return super().update(instance, validated_data)
      

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model =CartItem
        fields = '__all__'