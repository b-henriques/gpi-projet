from Commandes.models import Commande
from django.db import models

# Create your models here.
class Anomalie(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    
    type_erreur_montant = "Erreur sur le montant"
    type_erreur_moyen_paiement = "Probleme sur le moyen de paiement"
    type_choix = (
        (type_erreur_montant, "Erreur sur le montant"),
        (type_erreur_moyen_paiement, "Probleme sur le moyen de paiement")
    )

    type = models.CharField(
        max_length=45, choices=type_choix, default=type_erreur_montant)
    
    date_generation = models.DateField()
    courrier = models.BooleanField(default=False)