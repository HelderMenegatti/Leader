from django.db import models
from core.models import BaseModel


class Product(models.Model):

    UNIT_MEASUREMENT_CHOICES = [
        ("unit", "Unidades"),
        ("kilo", "Quilos"),
        ("liter", "Litros"),
    ]


    product_code = models.CharField(max_length=20, verbose_name="Código do Produto")
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    unit_measurement = models.CharField(max_length=20, choices=UNIT_MEASUREMENT_CHOICES)

    def __str__(self):
        return self.name


class PriceHistory(models.Model):
    product = models.ForeignKey(Product, related_name='price_history', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return f"{self.product.name} - {self.price} ({self.created_at})"


class Cart(models.Model):
    # user 
    products = models.ManyToManyField(Product, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    