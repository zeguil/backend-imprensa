# Generated by Django 4.0.5 on 2022-08-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_rename_referencia_edicoescomemorativas_nome_prod_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images/banner1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/banner1')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/banner1')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='images/banner1')),
            ],
        ),
        migrations.CreateModel(
            name='Banner2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images/banner2')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/banner2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/banner2')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='images/banner2')),
            ],
        ),
    ]
