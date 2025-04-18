# Generated by Django 3.2 on 2025-01-30 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'Принят'), ('2', 'Ожидает своей очереди'), ('3', 'Изготавливается'), ('4', 'Собирается'), ('5', 'Отправлен'), ('6', 'Доставлен'), ('7', 'Выдан')], default='1', max_length=8, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='order',
            name='track',
            field=models.CharField(blank=True, max_length=14, verbose_name='Почтовый трекер'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Адрес электронной почты'),
        ),
    ]
