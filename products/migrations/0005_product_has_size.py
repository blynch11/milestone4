# Generated by Django 3.2.9 on 2021-12-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_size',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
