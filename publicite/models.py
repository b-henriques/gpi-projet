from django.db import models
from referentiel.models import Article, Individu

# Create your models here.
class Publicite(models.Model):
    individus = models.ManyToManyField(Individu)
    articles = models.ManyToManyField(Article)
    titre = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    dateenvoi = models.DateTimeField()
    
