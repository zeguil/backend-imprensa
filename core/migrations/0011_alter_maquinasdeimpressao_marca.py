# Generated by Django 4.0.6 on 2022-07-27 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_maquinasdeimpressao_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinasdeimpressao',
            name='marca',
            field=models.CharField(default='', max_length=300),
        ),
    ]