from rest_framework import serializers
from core import models

class EdicoesComemorativasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EdicoesComemorativas
        fields = '__all__'
