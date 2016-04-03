# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20160403_0012'),
        ('comissao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comissao', models.PositiveIntegerField(verbose_name=b'Comiss\xc3\xa3o')),
                ('classe', models.ForeignKey(related_name='comisao_bonus_classe', verbose_name=b'Classe', to='comissao.Classe')),
                ('pedido', models.ForeignKey(verbose_name=b'Pedido', to='vendas.Pedido')),
            ],
        ),
    ]
