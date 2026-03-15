from django.contrib import admin
from .models import MonitoramentoFrota

@admin.register(MonitoramentoFrota)
class MonitoramentoFrotaAdmin(admin.ModelAdmin):
    list_display = ('total_onibus', 'eletricos', 'diesel', 'co2_evitado', 'data_atualizacao')