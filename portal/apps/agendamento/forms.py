from django import forms
from .models import Agendamento
from validate_docbr import CPF

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = [
            'nome_completo', 'data_nascimento', 'cpf', 'convenio',
            'sexo', 'data_agendamento', 'hora_agendamento', 'medico'
        ]
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'convenio': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'data_agendamento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_agendamento': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'medico': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        cpf_validator = CPF()

        # Remove qualquer formatação (ponto, hífen etc.)
        cpf_numerico = cpf_validator.filter_numbers(cpf)

        if not cpf_validator.validate(cpf_numerico):
            raise forms.ValidationError("CPF inválido.")

        return cpf_numerico  # salva apenas os números (ex: 12345678900)