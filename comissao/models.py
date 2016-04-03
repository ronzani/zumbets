# coding=utf-8
from django.db import models

CHOICES_CLASSE = ((1, 'I'),
                  (2, 'II'),
                  (3, 'III'),
                  (4, 'IV'),
                  (5, 'V'),)

class Classe(models.Model):
    numero = models.PositiveIntegerField(verbose_name='Número', choices=CHOICES_CLASSE)
    recrutas = models.PositiveIntegerField(verbose_name='Recrutas')
    bonus = models.PositiveIntegerField(verbose_name='Bônus')

    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'

    def __unicode__(self):
        return self.numero


class Nivel(models.Model):
    classe = models.ForeignKey('comissao.Classe', verbose_name='Classe')
    numero = models.PositiveIntegerField(verbose_name='Nível')
    comissao = models.PositiveIntegerField(verbose_name='Comissão')
    exp_minima = models.PositiveIntegerField(verbose_name='Experiência')
    condicao_sobrevivencia = models.PositiveIntegerField(verbose_name='Condição Sobrevivência')
    royalts = models.PositiveIntegerField(verbose_name='Royalts')

    class Meta:
        verbose_name = 'Nível'
        verbose_name_plural = 'Niveis'

    def __unicode__(self):
        return '%s - %s' %(self.classe, self.numero)


class Comissao(models.Model):
    pessoa = models.ForeignKey('distribuidor.Pessoa', verbose_name='Pessoa')
    pedido = models.ForeignKey('vendas.Pedido', verbose_name='Pedido')
    comissao = models.PositiveIntegerField(verbose_name='Comissão')
    exp = models.PositiveIntegerField(verbose_name='Experiência')
    data = models.DateTimeField(verbose_name='Data', auto_now=True)


    class Meta:
        verbose_name = 'Comissão'
        verbose_name_plural = 'Comissões'

    def __unicode__(self):
        return self.comissao


class Bonus(models.Model):
    classe = models.ForeignKey('comissao.Classe', verbose_name='Classe', related_name='comisao_bonus_classe')
    pedido = models.ForeignKey('vendas.Pedido',verbose_name='Pedido')
    comissao = models.PositiveIntegerField(verbose_name='Comissão')

