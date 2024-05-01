from rest_framework import serializers
from products.models import Product, PriceHistory


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    new_price = serializers.DecimalField(max_digits=10, decimal_places=2, write_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "product_code", 
            "name",
            "description",
            "unit_measurement",
            "price",
            "new_price",
        ]


    def get_price(self, obj):
        return obj.price_history.first().price


    def create(self, validated_data):
        new_price = validated_data.pop('new_price')
        product = Product.objects.create(**validated_data)
        PriceHistory.objects.create(product=product, price=new_price)
        return product


    def update(self, instance, validated_data):
        new_price = validated_data.pop('new_price')
        PriceHistory.objects.create(product=instance, price=new_price)
        return super().update(instance, validated_data)
      