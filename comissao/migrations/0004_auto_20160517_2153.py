# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0003_auto_20160418_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classe',
            name='bonus',
        ),
        migrations.RemoveField(
            model_name='comissao',
            name='exp',
        ),
        migrations.RemoveField(
            model_name='comissao',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='nivel',
            name='condicao_sobrevivencia',
        ),
        migrations.RemoveField(
            model_name='nivel',
            name='royalts',
        ),
        migrations.AddField(
            model_name='classe',
            name='exp_minima',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Experi\xc3\xaancia'),
            preserve_default=False,
        ),
    ]
