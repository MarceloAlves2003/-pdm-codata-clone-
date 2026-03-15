from ninja import Router, Schema
from django.db.models import Avg
from .models import Eixo
from typing import List

router = Router()

# Este é o formato que o JavaScript vai receber
class EixoSchema(Schema):
    titulo: str
    cor_hex: str  # <--- Tem que ser cor_hex
    slug_icone: str
    progresso_medio: float

@router.get("/eixos", response=List[EixoSchema])
def listar_eixos(request):
    eixos = Eixo.objects.all()
    resultado = []
    
    for e in eixos:
        # Calcula a média das metas ligadas a este eixo
        media = e.metas.aggregate(Avg('progresso'))['progresso__avg'] or 0
        
        resultado.append({
            "titulo": e.titulo,
            "cor_hex": e.cor_hex,
            "slug_icone": e.slug_icone,
            "progresso_medio": round(media, 1)
        })
        
    return resultado
