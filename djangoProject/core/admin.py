from .models import User
from django.contrib import admin

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'is_active', 'is_staff']


admin.site.register(User, UserAdmin)


