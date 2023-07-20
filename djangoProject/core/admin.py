from django.contrib import admin
from .models import Professor, Sala, Alocacao, User, Curso, Horario
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('id_user', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    list_display = ['id_user', 'is_active', 'is_staff', 'is_superuser']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    search_fields = ['id_user']
    ordering = ['id_user']
    filter_horizontal = ()
    readonly_fields = ['id_user']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id_user', 'password1', 'password2'),
        }),
    )


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    pass

@admin.register(Alocacao)
class AlocacaoAdmin(admin.ModelAdmin):
    pass

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    pass