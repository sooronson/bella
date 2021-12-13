from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from colorfield.fields import ColorField

from .file_name_generate import file_name_generator


class Category(models.Model):
    title = models.CharField(
        verbose_name=_('Имя категории'), max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, blank=True, related_name='child'
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'Categories'

    def __str__(self):
        if not self.parent:
            return f"Category: {self.title}"
        else:
            return f"{self.parent} --> {self.title}"


class Product(models.Model):
    category = models.ForeignKey(
        Category, verbose_name=_('Категория'),
        on_delete=models.CASCADE, related_name='category'
    )
    title = models.CharField(
        verbose_name=_('Наименование'), max_length=255, null=True
    )
    slug = models.SlugField(unique=True)
    description = models.TextField(
        verbose_name=_('Описание'), null=True, blank=True
    )
    price = models.DecimalField(
        verbose_name=_('Цена'), max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField(
        verbose_name=_('Количества'), default=0, null=True)
    article = models.CharField(
        verbose_name=_('Артикуль'), max_length=10, null=True)
    color = models.ForeignKey(
        'Color', verbose_name=_('Color'), on_delete=models.CASCADE,
        related_name='product_color', blank=True, null=True)
    size = models.CharField(
        verbose_name=_('Размер'), max_length=10, blank=True, null=True)
    discount = models.IntegerField(verbose_name=_('Скидка'), default=0)
    is_favorite = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']
        db_table = 'products'

    def __str__(self):
        return self.title

    @property
    def get_final_price(self):
        final_price = self.price - self.price * self.discount / 100
        return final_price


class Image(models.Model):
    product = models.ForeignKey(Product, related_name='product_image',
                                on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=_('Фото продукта'),
                              upload_to=file_name_generator,
                              )


class Favorite(models.Model):
    product = models.ManyToManyField(
        Product, related_name='favorite_products'
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)

    class Meta:
        db_table = 'favorite_products'


class Color(models.Model):
    title = models.CharField(verbose_name=_('Название цвета'), max_length=255)
    color = ColorField(default='#FFFFFF')

    class Meta:
        ordering = ['title']
        db_table = 'color'

    def __str__(self):
        return self.title


class Additional(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    key = models.CharField(max_length=300, null=True, blank=True)
    value = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        ordering = ['product']
        db_table = 'additional_info'
