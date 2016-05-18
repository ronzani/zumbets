from django.contrib import admin

from distribuidor.forms import PessoaForm
from distribuidor.models import *

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    model = Pessoa
    form = PessoaForm
    list_display = ['username', '__unicode__', 'exp', 'calcula_comissao', 'telefone1', 'email']
    fieldsets = [
                    ('Dados Pessoais', {'fields': (
                        ('first_name', 'last_name'),
                        ('email', 'sexo'),
                        ('data_nascimento', 'cpf'),
                        ('rg', 'orgao_emissor'),
                        ('telefone1', 'telefone2'),
                        ('estado', 'cidade'),
                        ('endereco', 'cep'),
                        ('recrutador'),
                    )}),

                    ('Dados de Usuario', {'fields': (
                        ('is_active', 'is_staff'),
                    )}),

                    ('Dados de Comissao', {'fields': (
                        ('exp', 'classe'),
                    )}),
                            ]


admin.site.register(Pessoa, PessoaAdmin)