# Generated by Django 4.0.3 on 2022-04-11 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
