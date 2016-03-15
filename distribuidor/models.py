# coding=utf-8
from django.contrib.auth.models import User
from django.db import models


CHOICES_SEXO = (('m', 'Masculino'),
                ('f', 'Feminino'),
                )


class Pessoa(User):
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    data_nascimento = models.DateField(verbose_name='Data Nascimento')
    sexo = models.CharField(max_length=1, verbose_name='Sexo', choices=CHOICES_SEXO)
    rg = models.CharField(max_length=30, verbose_name='RG')
    orgao_emissor = models.CharField(max_length=30, verbose_name='Orgão Emissor')
    estado = models.CharField(max_length=100, verbose_name='Estado')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    cep = models.PositiveIntegerField(verbose_name='CEP')
    endereco = models.CharField(max_length=100, verbose_name='Endereço')

    def __unicode__(self):
        return '%s' % self.get_full_name()

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
