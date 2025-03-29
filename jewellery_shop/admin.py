from django.contrib import admin
from .models import Category, Product, Gem, Gems_for_Products, Metal, Metals_for_Products, Collection, Finishing


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class FinishingAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Finishing, FinishingAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'collection', 'price', 'available', 'weight']
    list_filter = ['available', 'category', 'collection']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class GemAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'clarity', 'color']
    list_filter = ['clarity', 'color']
    list_editable = ['clarity']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Gem, GemAdmin)

class Gems_for_ProductsAdmin(admin.ModelAdmin):
    list_display = ['product', 'gem', 'weight', 'cut', 'count']
    list_editable = ['weight', 'count']
admin.site.register(Gems_for_Products, Gems_for_ProductsAdmin)

class MetalAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'alloy']
    list_filter = ['name']
    list_editable = ['alloy']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Metal, MetalAdmin)

class Metals_for_ProductsAdmin(admin.ModelAdmin):
    list_display = ['product', 'metal', 'weight']
    list_editable = ['weight']
admin.site.register(Metals_for_Products, Metals_for_ProductsAdmin)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Collection, CollectionAdmin)
