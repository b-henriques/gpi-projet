from django.core.validators import MinValueValidator
from django.db.models.deletion import CASCADE
from referentiel.models import Article, Individu
from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Create your models here.

class Commande(models.Model):
    client = ForeignKey(Individu, on_delete=CASCADE)

class Vente(models.Model):
    commande = ForeignKey(Commande, on_delete=CASCADE)
    article = ForeignKey(Article, on_delete=CASCADE)
    quantite = models.PositiveIntegerField()

class Reglement(models.Model):
    commande = ForeignKey(Commande, on_delete=CASCADE)
    numero = models.PositiveIntegerField()
    date = models.DateTimeField()
    montant = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    type_cheque = 'cheque'
    type_carte = 'carte'
    type_choix = ((type_cheque,'cheque'), (type_carte, 'carte'))

    banque = models.CharField(max_length=50, null=True, blank=True)

    date_expiration = models.DateField( null=True, blank=True)
    




