# Generated by Django 3.2 on 2025-01-25 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20250125_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=300, verbose_name='Адрес доставки'),
        ),
    ]
