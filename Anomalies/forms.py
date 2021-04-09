
from Commandes.models import Commande
from django import forms
from django.db.models import query
from django.forms.widgets import Input, Textarea
from .models import Anomalie
from referentiel.models import Individu


class FiltresForm(forms.Form):
    types = forms.MultipleChoiceField(choices=Anomalie.type_choix, required=False)
    date = forms.DateField(widget=Input({'type': 'date'}), required=False)
    individu = forms.ModelMultipleChoiceField(queryset=Individu.objects.all(), required=False)
    nCommande = forms.ModelMultipleChoiceField(queryset=Commande.objects.all(), required=False)


class CourrierForm(forms.Form):
    message = forms.CharField(widget=Textarea(attrs={'cols':80, 'rows':20}))