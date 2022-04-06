# Generated by Django 4.0.3 on 2022-04-06 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket_api', '0002_productpriceseller_remove_product_discount_percent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='selling_info',
            field=models.ManyToManyField(blank=True, related_name='products', through='supermarket_api.ProductPriceSeller', to='supermarket_api.seller'),
        ),
    ]