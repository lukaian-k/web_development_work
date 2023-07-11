from django.contrib import admin
from .models import Professor, Sala, Alocacao


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    pass

@admin.register(Alocacao)
class AlocacaoAdmin(admin.ModelAdmin):
    pass

