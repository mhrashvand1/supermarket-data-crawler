# Generated by Django 4.0.3 on 2022-04-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket_api', '0016_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='status'),
        ),
    ]
