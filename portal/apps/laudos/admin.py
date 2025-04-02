from django.contrib import admin
from .models import Laudo

@admin.register(Laudo)
class LaudoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'arquivo', 'enviado_em')
    search_fields = ('paciente__nome',)
