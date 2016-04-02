# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Data do Pedido', null=True),
        ),
    ]
