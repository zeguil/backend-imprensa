from rest_framework import viewsets
from core import models, serializers

class EdicoesComemorativasViewset(viewsets.ModelViewSet):
    queryset = models.EdicoesComemorativas.objects.all()
    serializer_class = serializers.EdicoesComemorativasSerializer

class Banner1Viewset(viewsets.ModelViewSet):
    queryset = models.Banner1.objects.all()
    serializer_class = serializers.Banner1Serializer

class Banner2Viewset(viewsets.ModelViewSet):
    queryset = models.Banner2.objects.all()
    serializer_class = serializers.Banner2Serializer

class CapasDoeViewset(viewsets.ModelViewSet):
    queryset = models.CapasDoe.objects.all()
    serializer_class = serializers.CapasDoeSerializer

class LinhatempoIoaViewset(viewsets.ModelViewSet):
    queryset = models.LinhatempoIoa.objects.all()
    serializer_class = serializers.LinhatempoIoaSerializer

class LinhatempoPresidentesViewset(viewsets.ModelViewSet):
    queryset = models.LinhatempoPresidentes.objects.all()
    serializer_class = serializers.LinhatempoPresidentesSerializer

class AtosRelevantesViewset(viewsets.ModelViewSet):
    queryset = models.AtosRelevantes.objects.all()
    serializer_class = serializers.AtosRelevantesSerializer

class MaquinasdeImpressaoViewset(viewsets.ModelViewSet):
    queryset = models.MaquinasdeImpressao.objects.all()
    serializer_class = serializers.MaquinasdeImpressaoSerializer


