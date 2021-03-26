from publicite.models import Cible
from referentiel.models import Individu
from publicite.forms import CibleForm, PubliciteForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import datetime

# Create your views here.
def index(request):
    return HttpResponse("<h1> Publicite </h1>")

def createPublicite(request):
    form = PubliciteForm(request.POST or None)
    if form.is_valid():
        form.save()
    contexte = {'form':PubliciteForm()}
    return render(request, 'publicite/createPublicite.html', contexte)

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