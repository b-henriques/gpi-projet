from referentiel.models import Article, Catcommerciale, Catprofessionnelle
from django import forms
from django.forms.models import ModelMultipleChoiceField, inlineformset_factory
from .models import Cible, Publicite

class PubliciteForm(forms.ModelForm):
    pass

class CibleForm(forms.Form):
    ageMin = forms.IntegerField(label="AgeMin:", min_value=18, max_value=100)
    ageMax = forms.IntegerField(label="AgeMax:", min_value=18, max_value=100)
    departementResidence = forms.IntegerField(label="Departement", min_value=0, max_value=100)
    catprofessionnelle = forms.ModelMultipleChoiceField(queryset=Catprofessionnelle.objects.all())
    catcommerciale = forms.ModelMultipleChoiceField(queryset=Catcommerciale.objects.all())