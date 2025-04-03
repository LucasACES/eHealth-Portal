from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Cria os grupos padrão: operacional e supervisor'

    def handle(self, *args, **kwargs):
        for nome in ['operacional', 'supervisor']:
            grupo, criado = Group.objects.get_or_create(name=nome)
            if criado:
                self.stdout.write(self.style.SUCCESS(f'Grupo "{nome}" criado com sucesso!'))
            else:
                self.stdout.write(f'Grupo "{nome}" já existe.')
