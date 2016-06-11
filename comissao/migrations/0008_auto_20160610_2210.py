# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20160403_0012'),
        ('comissao', '0007_auto_20160601_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalheComissao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.FloatField(verbose_name=b'Valor')),
                ('percentual', models.FloatField(verbose_name=b'Percentual')),
                ('valor_comissao', models.FloatField(verbose_name=b'Valor da Comiss\xc3\xa3o')),
                ('tipo', models.IntegerField(verbose_name=b'Tipo Comiss\xc3\xa3o')),
                ('comissao', models.ForeignKey(verbose_name=b'Comiss\xc3\xa3o', to='comissao.Comissao')),
                ('pedido', models.ForeignKey(verbose_name=b'Pedido', to='vendas.Pedido')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='detalhecomissao',
            unique_together=set([('pedido', 'tipo')]),
        ),
    ]
