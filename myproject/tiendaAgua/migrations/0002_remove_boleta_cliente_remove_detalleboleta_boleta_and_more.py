# Generated by Django 5.0.6 on 2024-06-27 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaAgua', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boleta',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='detalleboleta',
            name='boleta',
        ),
        migrations.RemoveField(
            model_name='detalleboleta',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Formulario',
        ),
        migrations.DeleteModel(
            name='Boleta',
        ),
        migrations.DeleteModel(
            name='DetalleBoleta',
        ),
    ]
