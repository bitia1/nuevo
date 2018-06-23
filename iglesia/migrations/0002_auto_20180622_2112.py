# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-22 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('iglesia', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='administracionministro',
            name='ministro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Ministro'),
        ),
        migrations.AddField(
            model_name='administracioncomisionproconstruccion',
            name='comision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.ComisionProConstruccion'),
        ),
        migrations.AddField(
            model_name='administracioncomisionproconstruccion',
            name='iglesia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iglesia.Iglesia'),
        ),
        migrations.AddField(
            model_name='administracioncomisioninventario',
            name='comision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.ComisionInventario'),
        ),
        migrations.AddField(
            model_name='administracioncomisioninventario',
            name='iglesia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iglesia.Iglesia'),
        ),
    ]
