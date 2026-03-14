from django.contrib import admin
from .models import Eixo, MetaReal  # O ponto antes de models é importante!

@admin.register(Eixo)
class EixoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cor_hex', 'slug_icone')

@admin.register(MetaReal)
class MetaRealAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'eixo', 'progresso')
    list_editable = ('progresso',)