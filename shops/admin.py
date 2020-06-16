from django.contrib import admin
from .models import *
from users.models import *


class ItemImageInline(admin.TabularInline):
    model = ItemImage


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Item._meta.fields]
    inlines = [ItemImageInline]

    class Meta:
        model = Item
#admin.site.register(Item, ItemAdmin)


class ItemImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ItemImage._meta.fields]

    class Meta:
        model = ItemImage


admin.site.register(ItemImage, ItemImageAdmin)


class ShopAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Shop._meta.fields]

    class Meta:
        model = Shop


admin.site.register(Shop, ShopAdmin)
admin.site.register(Category)

