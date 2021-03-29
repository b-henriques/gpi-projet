from Commandes.models import Reglement, Vente
from django import forms
from django.db.models.fields import CharField
from referentiel.models import Catprofessionnelle, Individu


class DateNaissance(forms.DateInput):
    input_type = 'date'


class CommandeFormIndividuConnu(forms.Form):
    nom = forms.CharField(max_length=50, label="Nom du client:")
    prenom = forms.CharField(max_length=50, label="Prénom du client :")
    ntel = forms.DecimalField(
        max_digits=10, decimal_places=0, label="Numéro de télephone :", min_value=0)


class CommandeFormIndividu(forms.Form):
    nom = forms.CharField(max_length=50, label="Nom du client:")
    prenom = forms.CharField(max_length=50, label="Prénom du client :")
    datenaissance = forms.DateField(
        label="Date de naissance :", widget=DateNaissance()
    )
    ntel = forms.DecimalField(
        max_digits=10, decimal_places=0, label="Numéro de télephone :", min_value=0)
    mail = forms.EmailField(label="Adresse mail :", required=False)
    numero = forms.IntegerField(label="Adresse N°:")
    rue = forms.CharField(max_length=100, label="Rue:")
    codepostal = forms.DecimalField(
        max_digits=5, decimal_places=0, label="Code postal :", min_value=0)
    ville = forms.CharField(max_length=50, label="Ville :")
    catprofessionnelle = forms.ModelChoiceField(
        queryset=Catprofessionnelle.objects.all())
    catcommerciale = forms.ChoiceField(
        choices=Individu.cat_choix, initial=Individu.prospect)


class CommandeArticleForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = ['article', 'quantite']


class CommandeChequeForm(forms.ModelForm):
    
    class Meta:
        model = Reglement
        fields = ['numero', 'montant', 'banque']


class CommandeCarteForm(forms.ModelForm):
    date_expiration = forms.DateField(
        label="Date du reglement :", widget=DateNaissance())

    class Meta:
        model = Reglement
        fields = ['numero', 'montant', 'date_expiration']
