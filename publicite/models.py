from django.db import models
from referentiel.models import Article, Individu

# Create your models here.

class Cible(models.Model):
    individus = models.ManyToManyField(Individu)
    valide = models.BooleanField(default=False)

class Publicite(models.Model):
    cible = models.ForeignKey(Cible, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    dateenvoi = models.DateTimeField(null=True)

    papierStandard = "PST"
    papierEconomique = "PEC"
    papierSuperieur = "PSU"
    internet = "INT"
    format_choix = [(papierStandard, "format papier standard"),
                    (papierEconomique, "format papier econimique"),
                    (papierSuperieur, "format papier superieur"),
                    (internet, "format internet")]

    format = models.CharField(
        max_length=3, choices=format_choix, default=papierStandard)

    articles = models.ManyToManyField(Article)
