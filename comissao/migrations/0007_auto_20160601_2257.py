# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0006_auto_20160601_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodoComissao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes_ano_referencia', models.DateField(verbose_name=b'Mes/Ano de Refer\xc3\xaancia')),
                ('inicio_periodo', models.DateField(verbose_name=b'Inicio do Periodo')),
                ('fim_periodo', models.DateField(verbose_name=b'Fim do Periodo')),
            ],
            options={
                'verbose_name': 'Periodo de Comiss\xe3o',
                'verbose_name_plural': 'Periodos de Comiss\xf5es',
            },
        ),
        migrations.AlterModelOptions(
            name='nivel',
            options={'ordering': ['numero'], 'verbose_name': 'N\xedvel', 'verbose_name_plural': 'Niveis'},
        ),
    ]
