from django.db import models
from apps.pacientes.models import Paciente

class Agendamento(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    nome_completo = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)  # Ex: 123.456.789-00
    convenio = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_agendamento = models.DateField()
    hora_agendamento = models.TimeField()
    medico = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_completo} - {self.data_agendamento} {self.hora_agendamento}"
