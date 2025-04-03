from django.urls import path
from . import views

urlpatterns = [
    path('', views.iti_validador, name='validador_iti'),
    path('listar/', views.lista_laudos, name='lista_laudos'), 
]

