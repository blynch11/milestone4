# Generated by Django 3.2.9 on 2021-11-23 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_category_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]