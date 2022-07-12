from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()

router.register('edicoes_come', viewsets.EdicoesComemorativasViewset)

urlpatterns = router.urls