# Generated by Django 4.0.6 on 2022-08-09 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_rename_image_edicoescomemorativas_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edicoescomemorativas',
            name='codigo',
            field=models.CharField(default='', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='edicoescomemorativas',
            name='data',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='edicoescomemorativas',
            name='referencia',
            field=models.CharField(default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='edicoescomemorativas',
            name='resumo',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]
