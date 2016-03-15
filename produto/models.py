# coding=utf-8
from django.db import models


CHOICES_MODELO = (('b', 'Babylook'),
                  ('n', 'Normal'),
                  )


class Camiseta(models.Model):
    tamanho = models.ForeignKey('produto.Tamanho', verbose_name='Tamanho')
    modelo = models.CharField(max_length=1, verbose_name='Modelo', choices=CHOICES_MODELO)
    cor = models.ForeignKey('produto.CorCamiseta', verbose_name='Cor')
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade')
    quantidade_reservada = models.PositiveIntegerField(verbose_name='Quantidade Reservada')

    def __unicode__(self):
        return '%s - %s - %s' % (self.modelo, self.tamanho, self.cor)

    def get_quantidade_disponivel(self):
        return self.quantidade - self.quantidade_reservada

    class Meta:
        verbose_name = 'Camiseta'
        verbose_name_plural = 'Camisetas'


class Referencia(models.Model):
    numero_referencia = models.CharField(max_length=100, verbose_name='Numero de Referência')
    cor = models.ForeignKey('produto.CorCamiseta', verbose_name='Cor da Camiseta')
    arte = models.ForeignKey('produto.Arte', verbose_name='Arte')
    preco = models.FloatField(verbose_name='Preço', blank=True, null=True)

    def __unicode__(self):
        return self.numero_referencia

    class Meta:
        verbose_name = 'Referência'
        verbose_name_plural = 'Referências'


class Arte(models.Model):
    modelo_arte = models.CharField(max_length=100, verbose_name='Modelo da Arte')
    cor_da_arte = models.CharField(max_length=100, verbose_name='Cor da Arte')

    def __unicode__(self):
        return '%s - %s' % (self.modelo_arte, self.cor_da_arte)

    class Meta:
        verbose_name = 'Arte'
        verbose_name_plural = 'Artes'


class Tamanho(models.Model):
    sigla = models.CharField(max_length=10, verbose_name='Sigla')
    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    altura = models.IntegerField(verbose_name='Altura', blank=True, null=True)
    largura = models.IntegerField(verbose_name='Largura', blank=True, null=True)

    def __unicode__(self):
        return '%s - %s' % (self.descricao, self.sigla)

    class Meta:
        verbose_name = 'Tamanho'
        verbose_name_plural = 'Tamanhos'


class CorCamiseta(models.Model):
    cor = models.CharField(max_length=100, verbose_name='Cor da Camiseta')

    def __unicode__(self):
        return self.cor

    class Meta:
        verbose_name = 'Cor da camiseta'
        verbose_name_plural = 'Cores das camisetas'


class Entrada(models.Model):
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade')
    produto = models.CharField(max_length=10, verbose_name='Produto')

    def __unicode__(self):
        return '%s - %d' % (self.produto, self.quantidade)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
