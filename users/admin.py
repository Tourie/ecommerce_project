from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UsersAdmin(UserAdmin):
    list_display = ('email', 'username', 'name', 'age', 'activity', 'date_joined', 'last_login')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, UsersAdmin)
# Register your models here.
