# Generated by Django 4.0.6 on 2022-07-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_linhatempoioa_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linhatempoioa',
            name='titulo',
            field=models.CharField(default='', max_length=70, null=True),
        ),
    ]