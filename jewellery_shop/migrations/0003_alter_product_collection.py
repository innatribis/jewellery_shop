# Generated by Django 3.2 on 2025-01-18 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jewellery_shop', '0002_auto_20250118_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='jewellery_shop.collection', verbose_name='Категория ювелирного изделия'),
        ),
    ]
