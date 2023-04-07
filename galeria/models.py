from django.db import models

# Create your models here.
class Fotografia(models.Model):
    CATEGORIAS = [
        ("ESTRELA", "Estrela"),
        ("GALAXIA", "Galáxia"),
        ("NEBULOSA", "Nebulosa"),
        ("PLANETA", "Planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=200, null=False, blank=False)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Fotografia -> [{self.nome}]"
