# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='telefone1',
            field=models.CharField(default='', max_length=16, verbose_name=b'Telefone1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='telefone2',
            field=models.CharField(max_length=16, null=True, verbose_name=b'Telefone2', blank=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(unique=True, max_length=11, verbose_name=b'CPF'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='orgao_emissor',
            field=models.CharField(max_length=30, verbose_name=b'Org\xc3\xa3o Emissor'),
        ),
    ]
