# Generated by Django 4.0.6 on 2022-07-28 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_capasdoe_resumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capasdoe',
            name='ano',
            field=models.CharField(max_length=15),
        ),
    ]
