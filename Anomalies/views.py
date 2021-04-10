from django.contrib.auth.decorators import permission_required
from django.urls.base import reverse
from django.urls.resolvers import get_ns_resolver
from Anomalies.forms import CourrierForm, FiltresForm
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Anomalie
from Commandes.models import Commande

# Create your views here.
@permission_required("utilisateurs.perm_anomalies")
def index(request):
    return render(request, 'anomalies/anomaliesHome.html')

@permission_required("utilisateurs.perm_anomalies")
def afficheAnomalies(request):
    """affichage et filtrage d'anoamlies
    """
    form = FiltresForm(request.POST or None)
    anomalies = Anomalie.objects.all()
    if form.is_valid():
        if form.cleaned_data['nCommande']:
            anomalies = anomalies.filter(
                commande__in=form.cleaned_data['nCommande'])
        if form.cleaned_data['date']:
            anomalies = anomalies.filter(
                date_generation=form.cleaned_data['date'])
        if form.cleaned_data['types']:
            anomalies = anomalies.filter(
                type__in=form.cleaned_data['types'])
        if form.cleaned_data['individu']:
            anomalies = anomalies.filter(
                commande__in=Commande.objects.filter(client__in=form.cleaned_data['individu']))
    context = {'anomalies': anomalies, 'form': form}
    return render(request, 'anomalies/afficheAnomalies.html', context)

@permission_required("utilisateurs.perm_anomalies")
def autresAnomalies(request, pk):
    """teste s'il y a d'autres anomalies associes à la meme commande ce cette anomalie(dont id=pk)
    """
    anomalie = get_object_or_404(Anomalie, pk=pk)
    anomalies = Anomalie.objects.filter(commande=anomalie.commande)
    anomalies = anomalies.filter(courrier=False)
    if len(anomalies) > 1:
        return render(request, 'anomalies/autresAnomalies.html', context={'commande': anomalie.commande.pk})
    else:
        return redirect(reverse('anomalies:envoiCourrier', args=[anomalie.commande.pk]))

@permission_required("utilisateurs.perm_anomalies")
def envoiCourrier(request, pk):
    """permet d'editer un message et transferrer un fichier xml au systeme d'edition
    """
    commande = get_object_or_404(Commande, pk=pk)
    anomalies = Anomalie.objects.filter(commande=commande)
    anomalies = anomalies.filter(courrier=False)
    form = CourrierForm(request.POST or None)
    if form.is_valid():
        print("valid form")
        # TODO: send xmlFile
    contexte = {'form': form, 'commande': commande, 'anomalies': anomalies}
    return render(request, 'anomalies/courrier.html', contexte)
