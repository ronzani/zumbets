# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0004_auto_20160517_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='nivel',
            name='exp_maxima',
            field=models.PositiveIntegerField(default=100, verbose_name=b'Experi\xc3\xaancia Maxima'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nivel',
            name='exp_minima',
            field=models.PositiveIntegerField(verbose_name=b'Experi\xc3\xaancia Minima'),
        ),
    ]
