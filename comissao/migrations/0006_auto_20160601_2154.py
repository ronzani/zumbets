# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0005_auto_20160601_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='exp_minima',
            field=models.BigIntegerField(verbose_name=b'Experi\xc3\xaancia'),
        ),
    ]
