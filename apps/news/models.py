from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=150)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    description = models.TextField(verbose_name='Описания', blank=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
