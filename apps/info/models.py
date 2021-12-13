from django.db import models
from solo.models import SingletonModel

from apps.info.file_name_generate import file_name_generator


class About(SingletonModel):
    title = models.CharField(verbose_name='Наименование', max_length=150,)

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title


class AboutDescription(models.Model):
    description = models.TextField(verbose_name='Описание')
    about_description = models.ForeignKey(
        "About", verbose_name='О нас',
        on_delete=models.CASCADE,
        related_name='about_descriptions'
    )

    def __str__(self):
        return self.description


class Image(models.Model):
    about = models.ForeignKey(
        About, verbose_name='О нас',
        on_delete=models.CASCADE, related_name='images_about'
    )
    image = models.ImageField(
        upload_to=file_name_generator, verbose_name='Фото'
    )

    class Meta:
        verbose_name = 'Картина'
        verbose_name_plural = 'Картины'


class Contact(SingletonModel):
    phone_number = models.CharField(verbose_name='Номер телефона',
                                    max_length=16)
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(
        verbose_name='Адрес',  max_length=255
    )
    ok = models.CharField(
        verbose_name='Одноклассники', max_length=255,
        blank=True, null=True
    )
    instagram = models.CharField(
        verbose_name='Instagram', max_length=255,
        blank=True, null=True
    )
    facebook = models.CharField(
        verbose_name='Facebook', max_length=255,
        blank=True, null=True

    )
    vk = models.CharField(
        verbose_name='VK', max_length=255,
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.phone_number

