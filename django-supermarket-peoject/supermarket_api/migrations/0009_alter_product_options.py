# Generated by Django 4.0.3 on 2022-04-11 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket_api', '0008_remove_product_main_image_mainimage_product_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['status', 'discount_percent']},
        ),
    ]
