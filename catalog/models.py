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
    issued_date = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    last_changed_date = models.DateTimeField(verbose_name='дата последнего изменения', auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('-issued_date',)


class Contacts(models.Model):
    country = models.CharField(max_length=100, verbose_name='Страна')
    inn = models.IntegerField(verbose_name='ИНН')
    address = models.CharField(max_length=100, verbose_name='Адрес')

    def __str__(self):
        return f'{self.country} {self.address}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Version(models.Model):
    product = models.ManyToManyField(Product, verbose_name='продукт', related_name='version')
    number = models.IntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.number} {self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
