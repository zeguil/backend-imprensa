# Generated by Django 4.0.6 on 2022-08-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_atosrelevantes_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atosrelevantes',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
