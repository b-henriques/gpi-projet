from django.db import models
from referentiel.models import Article, Individu

# Create your models here.


class Publicite(models.Model):
    individus = models.ManyToManyField(Individu)
    articles = models.ManyToManyField(Article)
    titre = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    dateenvoi = models.DateTimeField()

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
