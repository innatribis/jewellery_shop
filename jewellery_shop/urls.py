from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^collection/(?P<collection_slug>[-\w]+)/$', views.product_list, name='product_list_by_collection'),
    url(r'^finishing/(?P<finishing_slug>[-\w]+)/$', views.product_list, name='product_list_by_finishing'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
]
