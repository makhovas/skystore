from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание')

    # created_at = models.DateTimeField(verbose_name='дата создания', null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение(превью)', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    issued_date = models.DateTimeField(verbose_name='дата создания', null=True, blank=True)
    last_changed_date = models.DateTimeField(verbose_name='дата последнего изменения', null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)


class Contacts(models.Model):
    country = models.CharField(max_length=100, verbose_name='Страна')
    inn = models.IntegerField(verbose_name='ИНН')
    address = models.CharField(max_length=100, verbose_name='Адрес')

    def __str__(self):
        return f'{self.country} {self.address}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
