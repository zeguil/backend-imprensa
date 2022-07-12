from rest_framework import viewsets
from core import models, serializers

class EdicoesComemorativasViewset(viewsets.ModelViewSet):
    queryset = models.EdicoesComemorativas.objects.all()
    serializer_class = serializers.EdicoesComemorativasSerializer

class CapasDoeViewset(viewsets.ModelViewSet):
    queryset = models.CapasDoe.objects.all()
    serializer_class = serializers.CapasDoeSerializer

    
