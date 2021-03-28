from Commandes.models import Commande, Reglement, Vente
from django.contrib import admin

# Register your models here.
aRegistrer = [Commande, Vente, Reglement]
admin.site.register(aRegistrer)