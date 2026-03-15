from django.db import models

class MonitoramentoFrota(models.Model):
    total_onibus = models.IntegerField(default=0, verbose_name="Total da Frota")
    eletricos = models.IntegerField(default=0, verbose_name="Ônibus Elétricos")
    diesel = models.IntegerField(default=0, verbose_name="Ônibus a Diesel")
    co2_evitado = models.FloatField(default=0.0, verbose_name="CO2 Evitado (Toneladas)")
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Monitoramento da Frota"
        verbose_name_plural = "Monitoramento da Frota"

    def __str__(self):
        return f"Status da Frota em {self.data_atualizacao.strftime('%d/%m/%Y')}"
