# Generated by Django 4.0.5 on 2022-08-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_depoimentosservidores'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotosServidores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='images/fotos_servidores')),
                ('descricao', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Foto_Servidor',
                'verbose_name_plural': 'Fotos_Servidores',
                'db_table': 'foto_servidor',
                'managed': True,
            },
        ),
    ]
