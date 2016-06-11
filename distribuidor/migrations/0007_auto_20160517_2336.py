# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0004_auto_20160517_2153'),
        ('distribuidor', '0006_auto_20160517_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='nivel',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='classe',
            field=models.ForeignKey(default=1, verbose_name=b'Classe', to='comissao.Classe'),
            preserve_default=False,
        ),
    ]
