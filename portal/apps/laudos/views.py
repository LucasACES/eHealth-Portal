from django.http import JsonResponse, Http404
from .models import Laudo
from django.shortcuts import render, get_object_or_404
from apps.pacientes.models import Paciente
from django.contrib.auth.decorators import login_required

def iti_validador(request):
    secret_code = request.GET.get('_secretCode')
    formato = request.GET.get('_format')

    print(f"Recebido _secretCode: {secret_code}")
    print(f"Recebido _format: {formato}")

    # Validação flexível do formato
    if not secret_code or not formato or 'validador-iti' not in formato:
        raise Http404("Parâmetros inválidos")

    try:
        laudo = Laudo.objects.get(codigo_acesso=secret_code)
    except Laudo.DoesNotExist:
        raise Http404("Laudo não encontrado")

    url_pdf = request.build_absolute_uri(laudo.arquivo.url)

    response = {
        "version": "1.0.0",
        "prescription": {
            "signatureFiles": [
                {
                    "url": url_pdf
                }
            ]
        }
    }
    return JsonResponse(response)

@login_required
def laudos_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    laudos = Laudo.objects.filter(paciente=paciente).order_by('-enviado_em')
    return render(request, 'laudos/laudos_paciente.html', {'paciente': paciente, 'laudos': laudos})

@login_required
def lista_laudos(request):
    return render(request, 'laudos/lista.html')