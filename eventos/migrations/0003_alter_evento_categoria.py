# Generated by Django 5.2 on 2025-04-29 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_presenca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eventos.categoriaevento'),
        ),
    ]
