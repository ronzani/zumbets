# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidor', '0005_pessoa_nivel'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='exp',
            field=models.BigIntegerField(default=0, verbose_name=b'Experi\xc3\xaancia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='recrutador',
            field=models.ForeignKey(verbose_name=b'Recrutador', blank=True, to='distribuidor.Pessoa', null=True),
        ),
    ]
