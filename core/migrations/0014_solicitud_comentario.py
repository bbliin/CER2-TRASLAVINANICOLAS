# Generated by Django 5.2.1 on 2025-05-31 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_puntitos_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='comentario',
            field=models.TextField(default='Sin comentario', max_length=100),
        ),
    ]
