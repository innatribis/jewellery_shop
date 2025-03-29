from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^by/$', views.order_find_num, name='order_find_num'),
    url(r'^create/$', views.order_create, name='order_create'),
]
