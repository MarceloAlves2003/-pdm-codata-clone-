from django.db import models

class Eixo(models.Model):
    titulo = models.CharField(max_length=100)
    cor_hex = models.CharField(max_length=7)
    slug_icone = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

class MetaReal(models.Model):
    eixo = models.ForeignKey(Eixo, on_delete=models.CASCADE, related_name="metas")
    titulo = models.CharField(max_length=255)
    progresso = models.FloatField(default=0.0)

    def __str__(self):
        return self.titulo