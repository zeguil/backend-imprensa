from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()

router.register('edicoes_come', viewsets.EdicoesComemorativasViewset)
router.register('capas_doe', viewsets.CapasDoeViewset)
router.register('linhatempo_ioa', viewsets.LinhatempoIoa)

urlpatterns = router.urls