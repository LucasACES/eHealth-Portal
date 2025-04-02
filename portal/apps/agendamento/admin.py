from django.contrib import admin
from .models import Agendamento

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'data', 'horario', 'status')
    list_filter = ('status', 'data')
    search_fields = ('paciente__nome',)
