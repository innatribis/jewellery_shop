from django.db import models
from jewellery_shop.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator


class Order(models.Model):
    STATUSES = [
        ('1', 'Принят'),
        ('2', 'Ожидает своей очереди'),
        ('3', 'Изготавливается'),
        ('4', 'Собирается'),
        ('5', 'Отправлен'),
        ('6', 'Доставлен'),
        ('7', 'Выдан')
    ]
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    second_name = models.CharField(max_length=50, verbose_name='Отчество', blank=True)
    email = models.EmailField(verbose_name='Адрес электронной почты')
    address = models.CharField(max_length=300, verbose_name='Адрес доставки')
    postal_code = models.IntegerField(default=100000, validators=[MinValueValidator(100000), MaxValueValidator(999999)], verbose_name='Почтовый индекс')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(max_length=30, choices=STATUSES, verbose_name='Статус', default='1')
    track = models.CharField(max_length=14, verbose_name='Почтовый трекер', blank=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
