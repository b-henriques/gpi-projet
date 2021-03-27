from django.db.models.fields import NullBooleanField
from publicite.models import Cible, Publicite
from referentiel.models import Individu
from publicite.forms import CibleForm, PubliciteForm
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import datetime
from django.core import serializers
from django.urls import reverse


# Create your views here.
def index(request):
    return HttpResponse("<h1> Publicite </h1>")

def createPublicite(request):
    form = PubliciteForm(request.POST or None)
    if form.is_valid():
        form.save()
    contexte = {'form':PubliciteForm()}
    return render(request, 'publicite/editPublicite.html', contexte)

def createCible(request):
    form = CibleForm(request.POST or None)
    if form.is_valid():
        #individus = Individu.objects.filter(adresse.codepostal__startswith=form.cleaned_data['departementResidence'])
        individus = Individu.objects.filter(catprofessionnelle__in=form.cleaned_data['catprofessionnelle'] )
        individus = Individu.objects.filter(catcommerciale__in=form.cleaned_data['catcommerciale'] )
        individus = individus.filter(adresse__codepostal__startswith=form.cleaned_data['departementResidence'])
        anneeMax = datetime.date.today().year - form.cleaned_data['ageMin']
        anneeMin = datetime.date.today().year - form.cleaned_data['ageMax']
        individus = individus.filter(datenaissance__year__lte=anneeMax)
        individus = individus.filter(datenaissance__year__gte=anneeMin)
        if individus.count() == 0:
            individus = None
            contexte = {'form': form, 'individus': individus}
            return render(request, 'publicite/createCible.html', contexte)
        elif 'resultats' in request.POST:
            contexte = {'form': form, 'individus': individus}
            return render(request, 'publicite/createCible.html', contexte)
        else:
            c = Cible()
            c.save()
            c.individus.set(individus)
            return redirect('publicite:home')
    individus = None
    contexte = {'form': form, 'individus': individus}
    return render(request, 'publicite/createCible.html', contexte)

def validateCible(request):
    if 'valider' in request.POST:
        id = request.POST.get('valider')
        cible = Cible.objects.get(id=id)
        cible.valide = True
        cible.save()
        
    cibles = Cible.objects.filter(valide=False)
    contexte = {'cibles': cibles}
    return render(request, 'publicite/validateCible.html', contexte)

def envoiPublicite(request):
    publicites = Publicite.objects.filter(dateenvoi__isnull=True)
    contexte = {'publicites':publicites}
    return render(request, 'publicite/envoiPublicite.html', contexte)

def pubToXML(request, pk):
    publicite = get_object_or_404(Publicite, pk=pk)
    publicite.dateenvoi=datetime.datetime.now()
    publicite.save()
    XMLSerializer = serializers.get_serializer("xml")
    xml_serializer = XMLSerializer()
    with open("file.xml", "w") as out: xml_serializer.serialize(Publicite.objects.filter(pk=pk), stream=out)
    return redirect(reverse("publicite:creationPublicite"))

