from django.db import models

from apps.accounts.models import CustomUser
from apps.product.models import Product


class Order(models.Model):
    STATUS_CHOICES = (
        ('DELIVERED', 'доставлен'),
        ('SENT', 'отправлен'),
        ('CANCELED', 'отменен'),
    )
    user = models.ForeignKey(CustomUser,
                             on_delete=models.SET_NULL,
                             related_name='owners_order',
                             verbose_name='Покупатель',
                             null=True)
    address = models.CharField(verbose_name='Адрес доставки', max_length=255)
    create_at = models.DateField(verbose_name='Дата добавление в корзину',
                                 auto_now_add=True,)
    fnl_total_price = models.DecimalField(
        verbose_name='Общая цена Корзины',
        max_digits=9,
        decimal_places=2,
        default=0
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=12,
        default='SENT',
        null=True
    )
    price = models.DecimalField(
        verbose_name='Цена', max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.fnl_total_price} - {self.address}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              verbose_name='Заказ',
                              related_name='order_products')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='products'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество выбранного товара', default=1
    )

    def __str__(self):
        return f"{self.product} - {self.quantity}"

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
