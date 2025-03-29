from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include(('cart.urls','cart'), namespace='cart')),
    url(r'^orders/', include(('orders.urls','orders'), namespace='orders')),
    url(r'^', include(('jewellery_shop.urls', 'jewellery_shop'), namespace='jewellery_shop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


