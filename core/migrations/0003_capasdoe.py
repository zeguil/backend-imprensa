# Generated by Django 4.0.6 on 2022-07-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_edicoescomemorativas_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapasDoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('ano', models.CharField(max_length=10)),
                ('resumo', models.CharField(max_length=250)),
                ('capa', models.ImageField(blank=True, null=True, upload_to='images/capas')),
            ],
            options={
                'verbose_name': 'Capa Doe',
                'verbose_name_plural': 'Capas_Doe',
                'db_table': 'capa_doe',
                'managed': True,
            },
        ),
    ]
