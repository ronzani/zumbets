# coding=utf-8
from django.db import models


class Pedido(models.Model):
    CHOICE_STATUS_PEDIDO = (('1', 'Aguardando Pagamento'),
                            ('2', 'Em Produção'),
                            ('3', 'Concluido'),
                            ('4', 'Cancelado'),
                            )
    distribuidor = models.ForeignKey('distribuidor.Pessoa', verbose_name='Distribuidor')
    frete = models.FloatField(verbose_name='Frete', default=0)
    status = models.CharField(verbose_name='Status', max_length=1, choices=CHOICE_STATUS_PEDIDO, default='1')
    data = models.DateTimeField(verbose_name='Data do Pedido', auto_now=True, null=True)

    def __unicode__(self):
        return '%s' % self.distribuidor

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def get_preco_pedido(self):
        valor = 0
        if self.itenspedido_set.exists():
            for item in self.itenspedido_set.all():
                valor += item.preco * item.quantidade

        return valor+self.frete


class ItensPedido(models.Model):
    pedido = models.ForeignKey('vendas.Pedido', verbose_name='Pedido')
    referencia = models.ForeignKey('produto.Referencia', verbose_name='Referência')
    camiseta = models.ForeignKey('produto.Camiseta', verbose_name='Camiseta')
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade')
    preco_total = models.FloatField(verbose_name='Preço')
    cliente = models.CharField(max_length=100, verbose_name='Cliente')
    cpf_cliente = models.CharField(max_length=11, verbose_name='CPF')
    email_cliente = models.CharField(max_length=100, verbose_name='E-mail')
    endereco_cliente = models.CharField(max_length=100, verbose_name='Endereço')

    def __unicode__(self):
        return self.distribuidor

    class Meta:
        verbose_name = 'Itens no Pedido'
        verbose_name_plural = 'Itens nos Pedidos'

    def get_preco(self):
        return self.camiseta.preco
