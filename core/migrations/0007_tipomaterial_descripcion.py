# Generated by Django 5.2.1 on 2025-05-31 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_tipomaterial_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipomaterial',
            name='descripcion',
            field=models.TextField(default='Sin descripcion', max_length=100),
        ),
    ]
