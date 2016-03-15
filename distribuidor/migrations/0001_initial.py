# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.CharField(max_length=11, verbose_name=b'CPF')),
                ('data_nascimento', models.DateField(verbose_name=b'Data Nascimento')),
                ('sexo', models.CharField(max_length=1, verbose_name=b'Sexo', choices=[(b'm', b'Masculino'), (b'f', b'Feminino')])),
                ('rg', models.CharField(max_length=30, verbose_name=b'RG')),
                ('orgao_emissor', models.CharField(max_length=30, verbose_name=b'RG')),
                ('estado', models.CharField(max_length=100, verbose_name=b'Estado')),
                ('cidade', models.CharField(max_length=100, verbose_name=b'Cidade')),
                ('cep', models.PositiveIntegerField(verbose_name=b'CEP')),
                ('endereco', models.CharField(max_length=100, verbose_name=b'Endere\xc3\xa7o')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
