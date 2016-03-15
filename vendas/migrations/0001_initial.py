# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
        ('distribuidor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItensPedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantidade', models.PositiveIntegerField(verbose_name=b'Quantidade')),
                ('preco_total', models.FloatField(verbose_name=b'Pre\xc3\xa7o')),
                ('cliente', models.CharField(max_length=100, verbose_name=b'Cliente')),
                ('cpf_cliente', models.CharField(max_length=11, verbose_name=b'CPF')),
                ('email_cliente', models.CharField(max_length=100, verbose_name=b'E-mail')),
                ('endereco_cliente', models.CharField(max_length=100, verbose_name=b'Endere\xc3\xa7o')),
                ('camiseta', models.ForeignKey(verbose_name=b'Camiseta', to='produto.Camiseta')),
            ],
            options={
                'verbose_name': 'Itens no Pedido',
                'verbose_name_plural': 'Itens nos Pedidos',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('frete', models.FloatField(default=0, verbose_name=b'Frete')),
                ('status', models.CharField(default=b'1', max_length=1, verbose_name=b'Status', choices=[(b'1', b'Aguardando Pagamento'), (b'2', b'Em Produ\xc3\xa7\xc3\xa3o'), (b'3', b'Concluido'), (b'4', b'Cancelado')])),
                ('distribuidor', models.ForeignKey(verbose_name=b'Distribuidor', to='distribuidor.Pessoa')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.AddField(
            model_name='itenspedido',
            name='pedido',
            field=models.ForeignKey(verbose_name=b'Pedido', to='vendas.Pedido'),
        ),
        migrations.AddField(
            model_name='itenspedido',
            name='referencia',
            field=models.ForeignKey(verbose_name=b'Refer\xc3\xaancia', to='produto.Referencia'),
        ),
    ]
