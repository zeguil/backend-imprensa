from django.contrib import admin
from .models import (EdicoesComemorativas, Banner1, Banner2, CapasDoe,
                    LinhatempoIoa, LinhatempoPresidentes, AtosRelevantes,
                    MaquinasdeImpressao, DepoimentosServidores, FotosServidores)

admin.site.register(EdicoesComemorativas)
admin.site.register(Banner1)
admin.site.register(Banner2)
admin.site.register(CapasDoe)
admin.site.register(LinhatempoIoa)
admin.site.register(LinhatempoPresidentes)
admin.site.register(AtosRelevantes)
admin.site.register(MaquinasdeImpressao)
admin.site.register(DepoimentosServidores)
admin.site.register(FotosServidores)


