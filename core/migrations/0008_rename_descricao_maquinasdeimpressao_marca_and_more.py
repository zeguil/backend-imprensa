# Generated by Django 4.0.6 on 2022-07-26 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_maquinasdeimpressao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maquinasdeimpressao',
            old_name='descricao',
            new_name='marca',
        ),
        migrations.AddField(
            model_name='maquinasdeimpressao',
            name='status',
            field=models.CharField(default='', max_length=50),
        ),
    ]