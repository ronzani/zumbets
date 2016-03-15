# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modelo_arte', models.CharField(max_length=100, verbose_name=b'Modelo da Arte')),
                ('cor_da_arte', models.CharField(max_length=100, verbose_name=b'Cor da Arte')),
            ],
            options={
                'verbose_name': 'Arte',
                'verbose_name_plural': 'Artes',
            },
        ),
        migrations.CreateModel(
            name='Camiseta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modelo', models.CharField(max_length=1, verbose_name=b'Modelo', choices=[(b'b', b'Babylook'), (b'n', b'Normal')])),
                ('quantidade', models.PositiveIntegerField(verbose_name=b'Quantidade')),
                ('quantidade_reservada', models.PositiveIntegerField(verbose_name=b'Quantidade Reservada')),
            ],
            options={
                'verbose_name': 'Camiseta',
                'verbose_name_plural': 'Camisetas',
            },
        ),
        migrations.CreateModel(
            name='CorCamiseta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cor', models.CharField(max_length=100, verbose_name=b'Cor da Camiseta')),
            ],
            options={
                'verbose_name': 'Cor da camiseta',
                'verbose_name_plural': 'Cores das camisetas',
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantidade', models.PositiveIntegerField(verbose_name=b'Quantidade')),
                ('produto', models.CharField(max_length=10, verbose_name=b'Produto')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
            },
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_referencia', models.CharField(max_length=100, verbose_name=b'Numero de Refer\xc3\xaancia')),
                ('preco', models.FloatField(null=True, verbose_name=b'Pre\xc3\xa7o', blank=True)),
                ('arte', models.ForeignKey(verbose_name=b'Arte', to='produto.Arte')),
                ('cor', models.ForeignKey(verbose_name=b'Cor da Camiseta', to='produto.CorCamiseta')),
            ],
            options={
                'verbose_name': 'Refer\xeancia',
                'verbose_name_plural': 'Refer\xeancias',
            },
        ),
        migrations.CreateModel(
            name='Tamanho',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sigla', models.CharField(max_length=10, verbose_name=b'Sigla')),
                ('descricao', models.CharField(max_length=100, verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('altura', models.IntegerField(null=True, verbose_name=b'Altura', blank=True)),
                ('largura', models.IntegerField(null=True, verbose_name=b'Largura', blank=True)),
            ],
            options={
                'verbose_name': 'Tamanho',
                'verbose_name_plural': 'Tamanhos',
            },
        ),
        migrations.AddField(
            model_name='camiseta',
            name='cor',
            field=models.ForeignKey(verbose_name=b'Cor', to='produto.CorCamiseta'),
        ),
        migrations.AddField(
            model_name='camiseta',
            name='tamanho',
            field=models.ForeignKey(verbose_name=b'Tamanho', to='produto.Tamanho'),
        ),
    ]
