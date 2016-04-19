# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0002_bonus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comissao',
            name='comissao',
            field=models.FloatField(verbose_name=b'Comiss\xc3\xa3o'),
        ),
    ]
