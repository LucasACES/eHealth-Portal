from django.db import models
from apps.pacientes.models import Paciente
import uuid

class Laudo(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='laudos/')
    descricao = models.CharField(max_length=255, blank=True)
    codigo_acesso = models.CharField(max_length=32, unique=True)
    enviado_em = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.paciente and self.codigo_acesso:
            cpf = self.paciente.cpf.replace('.', '').replace('-', '')
            prefixo = cpf[:6]
            apenas_codigo = self.codigo_acesso.split('-')[-1]
            self.codigo_acesso = f"{prefixo}-{apenas_codigo}"
        super().save(*args, **kwargs)

