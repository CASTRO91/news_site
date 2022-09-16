from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    update_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', max_length=250, blank=True)
    is_published = models.BooleanField(default=True, verbose_name='публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT,  blank=True, verbose_name='Категория')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='наименование категорий')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'
        ordering = ['title']
