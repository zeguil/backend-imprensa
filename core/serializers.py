from rest_framework import serializers
from core import models

class EdicoesComemorativasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EdicoesComemorativas
        fields = '__all__'

class CapasDoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CapasDoe
        fields = '__all__'

