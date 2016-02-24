# coding=utf-8
from django.contrib.auth.models import User
from django.db import models

CHOICES_SEXO = (('m', 'Masculino'),
                ('f', 'Feminino'),
                )

class Nivel(models.Model):
    nivel = models.IntegerField(verbose_name='Nível')
    exp_minimo = models.IntegerField(verbose_name='Experiência Mínima')
    exp_maximo = models.IntegerField(verbose_name='Experiência Máxima')
    vendas_minimas = models.IntegerField(verbose_name='Vendas Mínimas')

    def __str__(self):
        return '%d' % self.nivel

    class Meta:
        verbose_name = 'Nível'
        verbose_name_plural = 'Níveis'


class Pessoa(User):
    data_nascimento = models.DateField(verbose_name='Data Nascimento')
    sexo = models.CharField(max_length=1, verbose_name='Sexo', choices=CHOICES_SEXO)
    nivel = models.ForeignKey('pedidos.Nivel', verbose_name='Nível')

    # def __str__(self):
    #     return self.get_full_name()

    def __unicode__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


class Tamanho(models.Model):
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    sigla = models.CharField(max_length=5, verbose_name='Sigla')
    altura = models.IntegerField(verbose_name='Altura', blank=True, null=True)
    largura = models.IntegerField(verbose_name='Largura', blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.descricao, self.sigla)

    class Meta:
        verbose_name = 'Tamanho'
        verbose_name_plural = 'Tamanhos'


class Produto(models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    preco = models.FloatField(verbose_name='Preço')
    # tamanho = models.ForeignKey('pedidos.Tamanho', verbose_name='Tamanho')

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
