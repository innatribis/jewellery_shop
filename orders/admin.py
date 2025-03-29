from django.contrib import admin
from .models import Order, OrderItem
from django.contrib import admin
from django.db.models import F, Q
from .tasks import order_sent, order_came

@admin.action(description="Обновить статус заказов")
def upd_status(modeladmin, request, queryset):
    right_orders = queryset.filter(~Q(status='7'))
    sent_orders = queryset.filter(status='4')
    came_orders = queryset.filter(status='5')
    for sent_order in sent_orders:
        order_sent.delay(sent_order.id)
    for came_order in came_orders:
        order_came.delay(came_order.id)
    right_orders.update(status=F('status') + 1)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'email',
                    'created',
                    'updated', 'track']
    list_filter = ['status', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [upd_status]
    readonly_fields = ('updated', 'created',)

admin.site.register(Order, OrderAdmin)
