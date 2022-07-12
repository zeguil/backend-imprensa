from django.db import models

# Create your models here.

class EdicoesComemorativas(models.Model):
    codigo = models.CharField(max_length=25)
    resumo = models.CharField(max_length=500)
    data = models.CharField(max_length=10)
    referencia = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = 'edicao_come'
        verbose_name = 'Edicao_Come'
        verbose_name_plural = 'Edicoes_Come'