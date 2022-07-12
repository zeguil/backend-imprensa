from distutils.command.upload import upload
from django.db import models

# Create your models here.

class EdicoesComemorativas(models.Model):
    codigo = models.CharField(max_length=25)
    resumo = models.CharField(max_length=500)
    data = models.CharField(max_length=10)
    referencia = models.CharField(max_length=300)
    image = models.ImageField(
        upload_to='images/edicoes', blank=True, null=True
    )

    class Meta:
        managed = True
        db_table = 'edicao_come'
        verbose_name = 'Edicao_Come'
        verbose_name_plural = 'Edicoes_Come'


class CapasDoe(models.Model):
    titulo = models.CharField(max_length=30)
    ano = models.CharField(max_length=10)
    resumo = models.CharField(max_length=250)
    capa = models.ImageField(
        upload_to='images/capas', blank=True, null=True
    )

    class Meta: 
        managed = True
        db_table = 'capa_doe'
        verbose_name = 'Capa Doe'
        verbose_name_plural = 'Capas_Doe'

class LinhatempoIoa(models.Model):
    ano = models.CharField(max_length=10)
    descricao = models.CharField(max_length=300)
    foto =  models.ImageField(
        upload_to='images/timeline_ioa', blank=True, null=True
    )

    class Meta:
        managed = True
        db_table = 'linhatempo_ioa'
        verbose_name = 'Linha Tempo Ioa'
        verbose_name_plural = 'Linhas do Tempo Ioa'

class LinhatempoPresidentes(models.Model):
    ano = models.CharField(max_length=10)
    descricao = models.CharField(max_length=300)
    icon = models.ImageField(
        upload_to='images/timeline_presidentes'
    )

    class Meta:
        managed = True
        db_table = 'linhatempo_presidente'
        verbose_name = 'Linha Tempo Presidente'
        verbose_name_plural = 'Linhas do Tempo Presidentes'
