from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import date
from apps.pacientes.models import Paciente
from apps.laudos.models import Laudo
from apps.agendamento.models import Agendamento
from django.contrib.auth.models import User

def acesso_negado(request):
    return render(request, 'usuarios/acesso_negado.html')

def logout_agradecimento(request):
    return render(request, 'usuarios/logout_agradecimento.html')


@login_required
def dashboard(request):
    total_pacientes = Paciente.objects.count()
    total_laudos = Laudo.objects.count()

    hoje = date.today()
    agendamentos_hoje = Agendamento.objects.filter(data=hoje).count()

    ultimos_laudos = Laudo.objects.select_related('paciente').order_by('-enviado_em')[:5]

    return render(request, 'usuarios/dashboard.html', {
        'total_pacientes': total_pacientes,
        'total_laudos': total_laudos,
        'agendamentos_hoje': agendamentos_hoje,
        'ultimos_laudos': ultimos_laudos,
    })

@login_required
def lista_usuarios(request):
    if request.user.groups.first().name != 'supervisor':
        return redirect('dashboard')
    
    usuarios = User.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

def home_redirect(request):
    if request.user.is_authenticated:
        destino = 'dashboard'
    else:
        destino = 'login'
    return render(request, 'usuarios/home_redirect.html', {'destino': destino})