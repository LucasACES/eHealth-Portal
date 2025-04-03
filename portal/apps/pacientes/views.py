from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Paciente

@login_required
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista.html', {'pacientes': pacientes})

@login_required
def novo_paciente(request):
    return render(request, 'pacientes/novo.html') 