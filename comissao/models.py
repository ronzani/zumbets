# coding=utf-8
from django.db import models
from django.utils.translation import ugettext as _

CHOICES_CLASSE = ((1, 'I'),
                  (2, 'II'),
                  (3, 'III'),
                  (4, 'IV'),
                  (5, 'V'),)

class Classe(models.Model):
    numero = models.PositiveIntegerField(verbose_name='Número', choices=CHOICES_CLASSE)
    recrutas = models.PositiveIntegerField(verbose_name='Recrutas')
    exp_minima = models.BigIntegerField(verbose_name='Experiência')
    # bonus = models.PositiveIntegerField(verbose_name='Bônus')

    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'

    def __unicode__(self):
        return '%s' %self.get_numero_display()


class Nivel(models.Model):
    classe = models.ForeignKey('comissao.Classe', verbose_name='Classe')
    numero = models.PositiveIntegerField(verbose_name='Nível')
    comissao = models.PositiveIntegerField(verbose_name='Comissão')
    exp_minima = models.PositiveIntegerField(verbose_name='Experiência Minima')
    exp_maxima = models.PositiveIntegerField(verbose_name='Experiência Maxima')
    # condicao_sobrevivencia = models.PositiveIntegerField(verbose_name='Condição Sobrevivência')
    # royalts = models.PositiveIntegerField(verbose_name='Royalts')

    class Meta:
        verbose_name = 'Nível'
        verbose_name_plural = 'Niveis'
        ordering = ['numero']

    def __unicode__(self):
        return '%s - %s' %(self.classe, self.numero)


class Comissao(models.Model):
    pessoa = models.ForeignKey('distribuidor.Pessoa', verbose_name='Pessoa')
    comissao = models.FloatField(verbose_name='Comissão')
    data = models.DateTimeField(verbose_name='Data', auto_now=True)

    class Meta:
        verbose_name = 'Comissão'
        verbose_name_plural = 'Comissões'

    def __unicode__(self):
        return self.comissao

class DetalheComissao(models.Model):
    comissao = models.ForeignKey('comissao.Comissao', verbose_name='Comissão')
    pedido = models.ForeignKey('vendas.Pedido', verbose_name='Pedido')
    valor = models.FloatField(verbose_name='Valor')
    percentual = models.FloatField(verbose_name='Percentual')
    valor_comissao = models.FloatField(verbose_name='Valor da Comissão')
    tipo = models.IntegerField(verbose_name='Tipo Comissão')

    class Meta:
        unique_together = ['pedido', 'tipo']


class PeriodoComissao(models.Model):
    mes_ano_referencia = models.DateField(verbose_name='Mes/Ano de Referência')
    inicio_periodo = models.DateField(verbose_name='Inicio do Periodo')
    fim_periodo = models.DateField(verbose_name='Fim do Periodo')

    class Meta:
        verbose_name = 'Periodo de Comissão'
        verbose_name_plural = 'Periodos de Comissões'

    def __unicode__(self):
        return '%s/%s' % (_(self.mes_ano_referencia.strftime('%B')), self.mes_ano_referencia.strftime('%Y'))



class Bonus(models.Model):
    classe = models.ForeignKey('comissao.Classe', verbose_name='Classe', related_name='comisao_bonus_classe')
    pedido = models.ForeignKey('vendas.Pedido',verbose_name='Pedido')
    comissao = models.PositiveIntegerField(verbose_name='Comissão')

