# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0002_bonus'),
        ('distribuidor', '0004_auto_20160402_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='nivel',
            field=models.ForeignKey(default=1, verbose_name=b'Nivel', to='comissao.Nivel'),
            preserve_default=False,
        ),
    ]
