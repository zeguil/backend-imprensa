from distutils.command.upload import upload
from django.db import models

# Create your models here.
class EdicoesComemorativas(models.Model):
    codigo = models.CharField(max_length=25, default='', null=True)
    titulo = models.CharField(max_length=100, default='', null=True)
    data = models.CharField(max_length=10, default='', null=True)
    nome_prod= models.CharField(max_length=300, default='', null=True)
    procedencia = models.CharField(max_length=600, default='', null=True)
    resumo = models.CharField(max_length=600, default='', null=True)
    main_image = models.ImageField(
        upload_to='images/edicoes', blank=True, null=True
    )
    image1  = models.ImageField(
        upload_to='images/edicoes', blank=True, null=True
    )
    image2 = models.ImageField(
        upload_to='images/edicoes', blank=True, null=True
    )

    class Meta:
        managed = True
        db_table = 'edicao_come'
        verbose_name = 'Edicao_Come'
        verbose_name_plural = 'Edicoes_Come'

class Banner1(models.Model):
    image1  = models.ImageField(
        upload_to='images/banner1', blank=True, null=True
    ) 
    image2  = models.ImageField(
        upload_to='images/banner1', blank=True, null=True
    ) 
    image3  = models.ImageField(
        upload_to='images/banner1', blank=True, null=True
    )
    image4  = models.ImageField(
        upload_to='images/banner1', blank=True, null=True
    )

class Banner2(models.Model):
    image1  = models.ImageField(
        upload_to='images/banner2', blank=True, null=True
    )
    image2  = models.ImageField(
        upload_to='images/banner2', blank=True, null=True
    )
    image3  = models.ImageField(
        upload_to='images/banner2', blank=True, null=True
    )
    image4  = models.ImageField(
        upload_to='images/banner2', blank=True, null=True
    ) 


class CapasDoe(models.Model):
    titulo = models.CharField(max_length=30,  default='', null=True)
    ano = models.CharField(max_length=30)
    resumo = models.CharField(max_length=600)
    capa = models.ImageField(
        upload_to='images/capas', blank=True, null=True
    )

    class Meta: 
        managed = True
        db_table = 'capa_doe'
        verbose_name = 'Capa_Doe'
        verbose_name_plural = 'Capas_Doe'

class LinhatempoIoa(models.Model):
    titulo = models.CharField(max_length=70, default='', null=True)
    ano = models.CharField(max_length=10)
    descricao = models.CharField(max_length=600)
    foto =  models.ImageField(
        upload_to='images/timeline_ioa', blank=True, null=True
    )

    class Meta:
        managed = True
        db_table = 'linhatempo_ioa'
        verbose_name = 'Linhatempo_Ioa'
        verbose_name_plural = 'Linhasdotempo_Ioa'

class LinhatempoPresidentes(models.Model):
    nome = models.CharField(max_length=150, default='', null=True)
    ano = models.CharField(max_length=10)
    descricao = models.CharField(max_length=300, default='', null=True)
    icon = models.ImageField(
        upload_to='images/timeline_presidentes', blank=True, null=True
    )

    class Meta:
        managed = True
        db_table = 'linhatempo_presidente'
        verbose_name = 'Linhatempo_Presidente'
        verbose_name_plural = 'Linhatempo_Presidentes'

class AtosRelevantes(models.Model):
    image = models.ImageField(
        upload_to='images/atos_relevantes', blank=True, null=True
    )
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)
    link = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = 'ato_relevante'
        verbose_name = 'Ato_Relevante'
        verbose_name_plural = 'Atos_Relevantes'

class MaquinasdeImpressao(models.Model):
    image = models.ImageField(
        upload_to='images/maquinas_impressao', blank=True, null=True
    )
    titulo = models.CharField(max_length=50)
    ano = models.CharField(max_length=10)
    marca = models.CharField(max_length=300, default='', null=True)
    modelo = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=50, default='')
