from django.shortcuts import render
from .forms import AgendamentoForm
from django.contrib.auth.decorators import login_required

@login_required
def agendar_view(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'agendamento/sucesso.html')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamento/formulario.html', {'form': form})

def agendamento_publico_view(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'agendamento/sucesso_publico.html')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamento/formulario_publico.html', {'form': form})
