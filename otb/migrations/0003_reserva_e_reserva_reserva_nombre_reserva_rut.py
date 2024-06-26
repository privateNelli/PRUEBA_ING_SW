# Generated by Django 5.0.6 on 2024-06-11 04:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otb', '0002_alter_reserva_id_reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='e_reserva',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='reserva',
            name='nombre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nombre_reserva_set', to='otb.cliente'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='rut',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rut_reserva_set', to='otb.cliente'),
        ),
    ]
