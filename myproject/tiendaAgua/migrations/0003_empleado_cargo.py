# Generated by Django 5.0.6 on 2024-06-29 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaAgua', '0002_remove_boleta_cliente_remove_detalleboleta_boleta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='cargo',
            field=models.CharField(default='Empleado', max_length=100),
        ),
    ]
