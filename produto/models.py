# coding=utf-8
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

CHOICES_MODELO = (('b', 'Babylook'),
                  ('n', 'Norma'),
                  )


class Camiseta(models.Model):
    tamanho = models.ForeignKey('produto.Tamanho', verbose_name='Tamanho')
    modelo = models.CharField(max_length=1, verbose_name='Modelo', choices=CHOICES_MODELO)
    cor = models.ForeignKey('produto.CorCamiseta', verbose_name='Cor')

    def __unicode__(self):
        return '%s - %s - %s' % (self.modelo, self.tamanho, self.cor)

    class Meta:
        verbose_name = 'Camiseta'
        verbose_name_plural = 'Camisetas'


class Estoque(models.Model):
    camiseta = models.ForeignKey('produto.Camiseta', verbose_name='Camiseta')
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade')
    quantidade_reservada = models.PositiveIntegerField(verbose_name='Quantidade Reservada')

    def get_quantidade_disponivel(self):
        return self.quantidade - self.quantidade_reservada

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoque'


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
    camiseta = models.ForeignKey('produto.Camiseta', verbose_name='Camiseta')
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade')

    def __unicode__(self):
        return '%s - %d' % (self.camiseta, self.quantidade)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'


@receiver(post_save, sender=Entrada)
def signal_atualiza_estoque(sender, instance, **kwargs):
    try:
        camiseta = Estoque.objects.filter(camiseta=instance.camiseta).first()
        if not camiseta:
            camiseta = Estoque.objects.create(camiseta=instance.camiseta, quantidade=0, quantidade_reservada=0)
        camiseta.quantidade = camiseta.quantidade + instance.quantidade
        camiseta.save()
    except Exception, e:
        raise
