from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from Jewellery import settings
import random


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Заказ {} в Ювелирной мастерской'.format(order_id)
    message = '''{} {},\n\nВаш заказ от {} в Ювелирной мастерской был создан.\n
Номер вашего заказа: {}.\n\nС уважением,\nЮвелирная мастерская'''.format(order.first_name,
                                                 order.second_name,
                                                 order.created.date(),
                                                 order.id)
    mail_sent = send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [order.email])
    return mail_sent


@shared_task
def order_sent(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Заказ {} в Ювелирной мастерской'.format(order_id)
    message = '''{} {},\n\nВаш заказ номер {} от {} в Ювелирной мастерской был выслан вам Почтой России.\n
Почтовый трекер вашего заказа: {}.\n\nС уважением,\nЮвелирная мастерская'''.format(order.first_name,
                                                                                       order.second_name,
                                                                                       order.id,
                                                                                       order.created.date(),
                                                                                       order.track)
    mail_sent = send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [order.email])
    return mail_sent


@shared_task
def order_came(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Заказ {} в Ювелирной мастерской'.format(order_id)
    message = '''{} {},\n\nВаш заказ номер {} от {} в Ювелирной мастерской был доставлен вам Почтой России.\n
Почтовый трекер вашего заказа: {}.\n\nС уважением,\nЮвелирная мастерская'''.format(order.first_name,
                                                                                       order.second_name,
                                                                                       order.id,
                                                                                       order.created.date(),
                                                                                       order.track)
    mail_sent = send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [order.email])
    return mail_sent
