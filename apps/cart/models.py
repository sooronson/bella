from django.db import models
from django.contrib.auth import get_user_model
from apps.product.models import Product



class Cart(models.Model):

    user = models.OneToOneField(
        get_user_model(), null=True, verbose_name='Владелец',
        on_delete=models.CASCADE, unique=True
    )
    total_price = models.DecimalField(
        max_digits=9, default=0,
        decimal_places=2, verbose_name='Общая цена', 
        )
    in_order = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}'s cart"



class CartProduct(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE,
        related_name='cart_products'
        )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, 
        related_name='products_in_carts'
        )
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(
        max_digits=9, decimal_places=2, 
        null=True, blank=True
        )

    def __str__(self):
        return self.product.title

    def save(self, *args, **kwargs):
        self.total_price = self.quantity*self.product.price
        super().save(*args, **kwargs)







