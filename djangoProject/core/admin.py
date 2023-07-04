from core.models import User, SaladeAula
from django.contrib import admin

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'is_active', 'is_staff']

@admin.register(SaladeAula)
class SaladeAulaAdmin(admin.ModelAdmin):
    list_display = ['number', 'capacity', 'bloco']

admin.site.register(User, UserAdmin)


