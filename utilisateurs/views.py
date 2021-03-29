
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

#TODO: creation d'utilisateur

def logIn(request):
    if request.user.is_authenticated:
        return render(request, 'utilisateurs/noAccess.html', {'groupes': request.user.groups.values_list('name',flat = True)})
    message = False
    if 'logIn' in request.POST:
        identifiant = request.POST['identifiant']
        motdepass = request.POST['motdepass']
        utilisateur = authenticate(
            request, username=identifiant, password=motdepass)
        if utilisateur is not None:
            login(request, utilisateur)
            # succes = redirect a une page en fonction du groupe
            groupes = request.user.groups.values_list('name',flat = True)
            if 'referentiel' in groupes:
                return redirect(reverse('referentiel:home'))
            elif 'publicite' in groupes:
                return redirect(reverse('publicite:home'))
            elif 'commandes' in groupes:
                return redirect(reverse('commandes:home'))
            else: #TODO: redirect anomalies
                return redirect(reverse('anomalies:home'))
        else:
            message = True
    contexte = {'messageErreur': message}
    return render(request, 'utilisateurs/logIn.html', contexte)


def index(request):
    return redirect(reverse('utilisateurs:logIn'))

def logOut(request):
    logout(request)
    return redirect(reverse('utilisateurs:logIn'))
    