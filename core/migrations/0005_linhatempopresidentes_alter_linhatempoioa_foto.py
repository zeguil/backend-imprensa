# Generated by Django 4.0.6 on 2022-07-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_linhatempoioa'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinhatempoPresidentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=300)),
                ('icon', models.ImageField(upload_to='images/timeline_presidentes')),
            ],
            options={
                'verbose_name': 'Linha Tempo Presidente',
                'verbose_name_plural': 'Linhas do Tempo Presidentes',
                'db_table': 'linhatempo_presidente',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='linhatempoioa',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/timeline_ioa'),
        ),
    ]
