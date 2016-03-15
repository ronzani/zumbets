from django.contrib import admin

from distribuidor.forms import PessoaForm
from distribuidor.models import *

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    model = Pessoa
    # form = PessoaForm
    fieldsets = [
                    ('Dados Pessoais', {'fields': (
                        ('first_name', 'last_name'),
                        ('email', 'sexo'),
                        ('data_nascimento', 'cpf'),
                        ('rg', 'orgao_emissor'),
                        ('estado', 'cidade'),
                        ('endereco', 'cep'),
                    )}),

                    ('Dados de Usuario', {'fields': (
                        ('username', 'password'),
                        ('is_active', 'is_staff'),
                    )}),
                ]


admin.site.register(Pessoa, PessoaAdmin)