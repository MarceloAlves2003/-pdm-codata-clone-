from ninja import Router, Schema
from .models import MonitoramentoFrota

router = Router()

class FrotaSchema(Schema):
    total_onibus: int
    eletricos: int
    diesel: int
    co2_evitado: float
    porcentagem_eletrica: float

@router.get("/dados", response=FrotaSchema)
def get_dados_frota(request):
    monitoramento = MonitoramentoFrota.objects.order_by("-data_atualizacao").first()

    if not monitoramento:
        return {
            "total_onibus": 0,
            "eletricos": 0,
            "diesel": 0,
            "co2_evitado": 0.0,
            "porcentagem_eletrica": 0.0,
        }

    porcentagem = (monitoramento.eletricos / monitoramento.total_onibus * 100) if monitoramento.total_onibus > 0 else 0

    return {
        "total_onibus": monitoramento.total_onibus,
        "eletricos": monitoramento.eletricos,
        "diesel": monitoramento.diesel,
        "co2_evitado": monitoramento.co2_evitado,
        "porcentagem_eletrica": round(porcentagem, 2),
    }
