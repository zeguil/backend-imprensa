from rest_framework import serializers
from core import models

class EdicoesComemorativasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EdicoesComemorativas
        fields = '__all__'

class Banner1Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner1
        fields = '__all__'

class Banner2Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner2
        fields = '__all__'

class CapasDoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CapasDoe
        fields = '__all__'

class LinhatempoIoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LinhatempoIoa
        fields = '__all__'

class LinhatempoPresidentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LinhatempoPresidentes
        fields = '__all__'

class AtosRelevantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AtosRelevantes
        fields = '__all__'

class MaquinasdeImpressaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaquinasdeImpressao
        fields = '__all__'




