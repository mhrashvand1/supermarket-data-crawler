# Generated by Django 4.0.3 on 2022-04-12 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket_api', '0012_alter_brand_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=1000, unique=True, verbose_name='title'),
        ),
    ]
