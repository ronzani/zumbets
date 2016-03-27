# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantidade', models.PositiveIntegerField(verbose_name=b'Quantidade')),
                ('quantidade_reservada', models.PositiveIntegerField(verbose_name=b'Quantidade Reservada')),
            ],
            options={
                'verbose_name': 'Estoque',
                'verbose_name_plural': 'Estoque',
            },
        ),
        migrations.RemoveField(
            model_name='camiseta',
            name='quantidade',
        ),
        migrations.RemoveField(
            model_name='camiseta',
            name='quantidade_reservada',
        ),
        migrations.RemoveField(
            model_name='entrada',
            name='produto',
        ),
        migrations.AddField(
            model_name='entrada',
            name='camiseta',
            field=models.ForeignKey(default='', verbose_name=b'Camiseta', to='produto.Camiseta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estoque',
            name='camiseta',
            field=models.ForeignKey(verbose_name=b'Camiseta', to='produto.Camiseta'),
        ),
    ]
