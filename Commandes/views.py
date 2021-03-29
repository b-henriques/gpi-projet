from Anomalies.models import Anomalie
from datetime import date
from referentiel.forms import ArticleForm
from Commandes.forms import CommandeArticleForm, CommandeCarteForm, CommandeChequeForm, CommandeFormIndividu, CommandeFormIndividuConnu
from Commandes.models import Commande, Reglement, Vente
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from referentiel.models import Adresse, Individu
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request, 'referentiel/referentiel_view.html')


#TODO: paiement


def createCommandeIndividu(request):
    form = CommandeFormIndividuConnu(request.POST or None)
    if form.is_valid():
        try:
            individu = Individu.objects.get(
                nom=form.cleaned_data.get('nom'),
                prenom=form.cleaned_data.get('prenom'),
                ntel=form.cleaned_data.get('ntel')
            )
        except:
            return redirect(reverse('commandes:createCommandeIndividuNouveau'))
        else:
            commande = Commande(client=individu)
            commande.save()
            pk = commande.pk
            return redirect(reverse('commandes:createCommandeArticle', args=[pk]))
    contexte = {'form': form}
    return render(request, 'commandes/createCommande.html', contexte)


def createCommandeIndividuNouveau(request):
    form = CommandeFormIndividu(request.POST or None)
    if form.is_valid():
        adresse = Adresse(
            numero=form.cleaned_data['numero'],
            rue=form.cleaned_data['rue'],
            codepostal=form.cleaned_data['codepostal'],
            ville=form.cleaned_data['ville']
        )
        adresse.save()
        individu = Individu(
            nom=form.cleaned_data['nom'],
            prenom=form.cleaned_data['prenom'],
            datenaissance=form.cleaned_data['datenaissance'],
            ntel=form.cleaned_data['ntel'],
            mail=form.cleaned_data['mail'],
            adresse=adresse,
            catcommerciale=form.cleaned_data['catcommerciale'],
            catprofessionnelle=form.cleaned_data['catprofessionnelle'],
        )
        individu.save()
        commande = Commande(client=individu)
        commande.save()
        pk = commande.pk
        return redirect(reverse('commandes:createCommandeArticle', args=[pk]))
    contexte = {'form': form, 'message': "Nouveau Individu"}
    return render(request, 'commandes/createCommande.html', contexte)


def createCommandeArticle(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    articles = Vente.objects.filter(commande=commande)
    form = CommandeArticleForm(request.POST or None)
    if form.is_valid():
        if 'valider' in request.POST:
            vente = Vente(commande=commande, article=form.cleaned_data.get(
                'article'), quantite=form.cleaned_data.get('quantite'))
            vente.save()
            return redirect(reverse('commandes:createCommandeReglementChoix', args=[pk]))
        else:
            vente = Vente(commande=commande, article=form.cleaned_data.get(
                'article'), quantite=form.cleaned_data.get('quantite'))
            vente.save()
            contexte = {'form': form, 'message': "Ajout article",
                        'article': True, 'articles': articles}
            return render(request, 'commandes/createCommande.html', contexte)
    contexte = {'form': form, 'message': "Ajout article",
                'article': True, 'articles': articles}
    return render(request, 'commandes/createCommande.html', contexte)


def createCommandeReglementChoix(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    contexte = {'commande': commande.pk}
    return render(request, 'commandes/reglementChoix.html', contexte)


def createCommandeReglementCheque(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    form = CommandeChequeForm(request.POST or None)
    if form.is_valid():
        reglement = Reglement(commande=commande,
                              numero=form.cleaned_data.get('numero'),
                              date=date.today(),
                              montant=form.cleaned_data.get('montant'),
                              type=Reglement.type_cheque,
                              banque=form.cleaned_data.get('banque'),
                              )
        reglement.save()
        return redirect(reverse('commandes:createCommandeRecap', args=[pk]))

    contexte = {'form': form}
    return render(request, 'commandes/reglement.html', contexte)


def createCommandeReglementCarte(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    form = CommandeCarteForm(request.POST or None)
    if form.is_valid():
        reglement = Reglement(commande=commande,
                              numero=form.cleaned_data.get('numero'),
                              date=date.today(),
                              montant=form.cleaned_data.get('montant'),
                              type=Reglement.type_carte,
                              date_expiration=form.cleaned_data.get(
                                  'date_expiration'),

                              )
        reglement.save()
        return redirect(reverse('commandes:createCommandeRecap', args=[pk]))
    contexte = {'form': form}
    return render(request, 'commandes/reglement.html', contexte)


def commandeRecap(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    articles = Vente.objects.filter(commande=commande)
    reglement = Reglement.objects.get(commande=commande)
    contexte = {'commande': commande,
                'articles': articles, 'reglement': reglement}
    return render(request, 'commandes/commandeRecap.html', contexte)


def validiteCommande(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    articles = Vente.objects.filter(commande=commande)
    reglement = Reglement.objects.get(commande=commande)
    total = 0
    for a in articles:
        total += a.article.prix
    contexte = {'total': total, 'montant': reglement.montant}

    if 'valider' in request.POST:
        validite = True
        # execution des tests de validite
        # si montant non correct
        if total != reglement.montant:
            anomalie1 = Anomalie(
                commande=commande, type=Anomalie.type_erreur_montant, date_generation=date.today())
            anomalie1.save()
            validite = False
        # si cheque non signe
        if reglement.type == 'cheque':
            if 'chequeSigne' not in request.POST:
                anomalie2 = Anomalie(
                    commande=commande, type=Anomalie.type_erreur_moyen_paiement, date_generation=date.today())
                anomalie2.save()
                validite = False
        # TODO: verification numero carte
        commande.valide = validite
        return redirect(reverse('commandes:reponseValiditeCommande', args=[pk]))
    return render(request, 'commandes/validerCommande.html', contexte)

def reponseValiditeCommande(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    anomalies = Anomalie.objects.filter(commande=commande)
    contexte = {'valide': commande.valide, 'anomalies': anomalies}
    return render(request, 'commandes/reponseValiderCommande.html', contexte)