from django.contrib import admin
from products.models import Product, PriceHistory


class PriceHistoryInline(admin.TabularInline):
    model = PriceHistory
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = [
        "product_code",
        "name",
        "unit_measurement",
        "price",
    ]

    inlines = [PriceHistoryInline]

    def price(self, obj):
        last_price_history = obj.price_history.first()
        if last_price_history:
            return last_price_history.price
        return None


admin.site.register(PriceHistory)