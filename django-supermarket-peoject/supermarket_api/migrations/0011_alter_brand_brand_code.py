# Generated by Django 4.0.3 on 2022-04-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket_api', '0010_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_code',
            field=models.CharField(max_length=1000, unique=True, verbose_name='brand code'),
        ),
    ]