# Generated by Django 4.2.4 on 2023-09-27 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_version_product_version_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-issued_date',), 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AlterField(
            model_name='product',
            name='issued_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_changed_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата последнего изменения'),
        ),
    ]