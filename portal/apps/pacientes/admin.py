from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'data_nascimento', 'telefone', 'email')
    search_fields = ('nome', 'cpf')
