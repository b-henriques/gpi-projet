from referentiel.forms import ArticleForm
from Commandes.forms import CommandeFormIndividuConnu
from Commandes.models import Commande, Vente
from django.http.response import HttpResponse
from django.shortcuts import render
from referentiel.models import Individu

# Create your views here.
def index(request):
    return HttpResponse("<h1> Commandes </h1>")

#TODO: creation dindividu inconnu
#TODO: ajout article
#TODO: paiement



def createCommandeIndividu(request):
    form = CommandeFormIndividuConnu(request.POST or None)
    if form.is_valid():
        print("ok")
        individu = Individu.objects.get(
            nom = form.cleaned_data.get('nom'), 
            prenom = form.cleaned_data.get('prenom'), 
            ntel = form.cleaned_data.get('ntel')
            )
        if individu == None :
            print("Creation d'individu")
        else:
            commande = Commande(client=individu)
            print(commande.pk)
            commande.save()
            print(commande.pk)
    contexte = {'form' : form}
    return render(request, 'commandes/createCommande.html', contexte)
