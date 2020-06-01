from django.contrib import admin
from .models import *


class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Item._meta.fields]


admin.site.register(Shop)
admin.site.register(Item)

# Register your models here.
