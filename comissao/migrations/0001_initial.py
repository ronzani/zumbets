# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_pedido_data'),
        ('distribuidor', '0004_auto_20160402_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.PositiveIntegerField(verbose_name=b'N\xc3\xbamero', choices=[(1, b'I'), (2, b'II'), (3, b'III'), (4, b'IV'), (5, b'V')])),
                ('recrutas', models.PositiveIntegerField(verbose_name=b'Recrutas')),
                ('bonus', models.PositiveIntegerField(verbose_name=b'B\xc3\xb4nus')),
            ],
            options={
                'verbose_name': 'Classe',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Comissao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comissao', models.PositiveIntegerField(verbose_name=b'Comiss\xc3\xa3o')),
                ('exp', models.PositiveIntegerField(verbose_name=b'Experi\xc3\xaancia')),
                ('data', models.DateTimeField(auto_now=True, verbose_name=b'Data')),
                ('pedido', models.ForeignKey(verbose_name=b'Pedido', to='vendas.Pedido')),
                ('pessoa', models.ForeignKey(verbose_name=b'Pessoa', to='distribuidor.Pessoa')),
            ],
            options={
                'verbose_name': 'Comiss\xe3o',
                'verbose_name_plural': 'Comiss\xf5es',
            },
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.PositiveIntegerField(verbose_name=b'N\xc3\xadvel')),
                ('comissao', models.PositiveIntegerField(verbose_name=b'Comiss\xc3\xa3o')),
                ('exp_minima', models.PositiveIntegerField(verbose_name=b'Experi\xc3\xaancia')),
                ('condicao_sobrevivencia', models.PositiveIntegerField(verbose_name=b'Condi\xc3\xa7\xc3\xa3o Sobreviv\xc3\xaancia')),
                ('royalts', models.PositiveIntegerField(verbose_name=b'Royalts')),
                ('classe', models.ForeignKey(verbose_name=b'Classe', to='comissao.Classe')),
            ],
            options={
                'verbose_name': 'N\xedvel',
                'verbose_name_plural': 'Niveis',
            },
        ),
    ]
