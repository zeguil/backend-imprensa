# Generated by Django 4.0.6 on 2022-08-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_linhatempopresidentes_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linhatempopresidentes',
            name='descricao',
            field=models.CharField(default='', max_length=300, null=True),
        ),
    ]