from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()

router.register('edicoes_come', viewsets.EdicoesComemorativasViewset)
router.register('capas_doe', viewsets.CapasDoeViewset)
router.register('linhatempo_ioa', viewsets.LinhatempoIoaViewset)
router.register('linhatempo_presidentes', viewsets.LinhatempoPresidentesViewset)
router.register('atos_relevantes', viewsets.AtosRelevantesViewset)
router.register('maquinas_impressao', viewsets.MaquinasdeImpressaoViewset)

urlpatterns = router.urls