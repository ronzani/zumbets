# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produto', '0002_auto_20160402_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaidaManual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantidade', models.PositiveIntegerField(verbose_name=b'Quantidade')),
                ('justificativa', models.TextField(max_length=500, verbose_name=b'Justificativa')),
                ('camiseta', models.ForeignKey(verbose_name=b'Camiseta', to='produto.Camiseta')),
                ('usuario', models.ForeignKey(verbose_name='Usu\xe1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Saida',
                'verbose_name_plural': 'Saidas',
            },
        ),
    ]
