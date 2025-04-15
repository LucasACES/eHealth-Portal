from django.urls import path
from .views import agendar_view, agendamento_publico_view

urlpatterns = [
    path('agendar/', agendar_view, name='agendar'),  # versão interna
    path('publico/', agendamento_publico_view, name='agendamento_publico'),  # versão pública
]
 