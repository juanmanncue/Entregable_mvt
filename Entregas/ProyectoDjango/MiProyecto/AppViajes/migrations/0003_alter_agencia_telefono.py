# Generated by Django 4.1.2 on 2022-11-14 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppViajes', '0002_remove_agencia_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencia',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
    ]