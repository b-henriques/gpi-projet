from django.forms.widgets import Textarea
from referentiel.models import Article, Catprofessionnelle, Individu
from django import forms
from django.forms.models import ModelMultipleChoiceField, inlineformset_factory
from .models import Cible, Publicite


class PubliciteForm(forms.ModelForm):

    description = forms.CharField(
        label="Description", widget=Textarea(attrs={'rows': '10', 'cols': '40'}))

    class Meta:
        model = Publicite
        fields = ['titre', 'description', 'cible', 'articles']

    def clean(self):
        data = super().clean()
        if(len(self.cleaned_data['articles']) > 5 or len(self.cleaned_data['articles']) == 0):
            self._errors['articles'] = self.error_class([
                "Nombre d'articles doit etre superieur à 0 et inferieur ou égal à 5 "])


class CibleForm(forms.Form):
    ageMin = forms.IntegerField(label="AgeMin:", min_value=18, max_value=100)
    ageMax = forms.IntegerField(label="AgeMax:", min_value=18, max_value=100)
    departementResidence = forms.IntegerField(
        label="Departement", min_value=0, max_value=100)
    catprofessionnelle = forms.ModelMultipleChoiceField(
        queryset=Catprofessionnelle.objects.all())
    catcommerciale = forms.MultipleChoiceField(choices=Individu.cat_choix)

    def clean(self):
        data = super().clean()
        if self.cleaned_data.get('ageMax') < self.cleaned_data.get('ageMin'):
            self._errors['ageMax'] = self.error_class([
                'Age Maximale doit etre superieure à age minimale'])
        return data
