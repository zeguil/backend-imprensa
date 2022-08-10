# Generated by Django 4.0.6 on 2022-08-09 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_atosrelevantes_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edicoescomemorativas',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='edicoescomemorativas',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/edicoes'),
        ),
        migrations.AddField(
            model_name='edicoescomemorativas',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/edicoes'),
        ),
    ]
