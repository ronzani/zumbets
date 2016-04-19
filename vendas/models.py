# coding=utf-8
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from comissao.models import Comissao
from produto.models import Estoque


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

        return valor


@receiver(post_save, sender=Pedido)
def signal_post_save_pedido(sender, instance, **kwargs):
    if instance.status == '3':  # Pedido concluido
        if instance.itenspedido_set.exists():
            for item in instance.itenspedido_set.all():
                # Da baixa no estoque
                estoque = Estoque.objects.filter(camiseta=item.camiseta).first()
                if estoque:
                    estoque.quantidade_reservada = estoque.quantidade_reservada - item.quantidade
                    estoque.quantidade = estoque.quantidade - item.quantidade
                    estoque.save()

        #Calcula a comissão do distribuidor
        percent_comissao = float(instance.distribuidor.nivel.comissao)/100
        comissao = instance.get_preco_pedido() * percent_comissao
        Comissao.objects.create(pessoa=instance.distribuidor, pedido=instance, comissao=comissao, exp=0)
    elif instance.status == '4':  # Pedido Cancelado
        if instance.itenspedido_set.exists():
            for item in instance.itenspedido_set.all():
                # Devolve iten para o estoque
                estoque = Estoque.objects.filter(camiseta=item.camiseta).first()
                if estoque:
                    estoque.quantidade_reservada = estoque.quantidade_reservada - item.quantidade
                    estoque.save()


class ItensPedido(models.Model):
    pedido = models.ForeignKey('vendas.Pedido', verbose_name='Pedido')
    referencia = models.ForeignKey('produto.Referencia', verbose_name='Referência')
    camiseta = models.ForeignKey('produto.Camiseta', verbose_name='Camiseta')
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade')
    preco = models.FloatField(verbose_name='Preço')
    cliente = models.CharField(max_length=100, verbose_name='Cliente')
    cpf_cliente = models.CharField(max_length=11, verbose_name='CPF')
    email_cliente = models.CharField(max_length=100, verbose_name='E-mail')
    endereco_cliente = models.CharField(max_length=100, verbose_name='Endereço')

    def __unicode__(self):
        return '%s' % self.referencia

    class Meta:
        verbose_name = 'Itens no Pedido'
        verbose_name_plural = 'Itens nos Pedidos'

    def get_preco(self):
        return self.camiseta.preco

    def get_preco_total_item(self):
        return self.quantidade * self.get_preco()


@receiver(post_save, sender=ItensPedido)
def signal_post_save_itens_pedido(sender, instance, **kwargs):
    if instance.pedido.status == '1':  # Pedido aberto
        # Atualiza a quantidade reservada do estoque
        estoque = Estoque.objects.filter(camiseta=instance.camiseta).first()
        if estoque:
            estoque.quantidade_reservada = estoque.quantidade_reservada + instance.quantidade
            estoque.save()