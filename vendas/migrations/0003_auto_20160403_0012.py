# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_pedido_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itenspedido',
            old_name='preco_total',
            new_name='preco',
        ),
    ]
