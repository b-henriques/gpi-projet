from django import forms
from .models import Article, Catcommerciale, Catprofessionnelle


class ArticleForm(forms.ModelForm):
    prix = forms.DecimalField(max_digits=6, decimal_places=2, label="Prix :", min_value=0)
    class Meta:
        model = Article
        fields = '__all__'


class IndividuForm(forms.Form):
    nom = forms.CharField(max_length=50, label= "Nom de l'utilisateur:")
    prenom = forms.CharField(max_length=50, label="Prénom de l'utilisateur :")
    datenaissance = forms.DateField(label="Date de naissance :")
    ntel = forms.DecimalField(max_digits=10, decimal_places=0, label="Numéro de télephone :", min_value=0)
    mail = forms.EmailField(label="Adresse mail :", required= False)
    numero = forms.IntegerField(label="Adresse N°:")
    rue = forms.CharField(max_length=100, label="Rue:")
    codepostal = forms.DecimalField(max_digits=5, decimal_places=0, label="Code postal :", min_value=0)
    ville = forms.CharField(max_length=50, label="Ville :")
    catprofessionnelle = forms.ModelChoiceField(queryset=Catprofessionnelle.objects.all())
    catcommerciale = forms.ModelChoiceField(queryset=Catcommerciale.objects.all())

