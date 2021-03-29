
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your views here.


def logIn(request):
    message = False
    if 'logIn' in request.POST:
        identifiant = request.POST['identifiant']
        motdepass = request.POST['motdepass']
        utilisateur = authenticate(
            request, username=identifiant, password=motdepass)
        if utilisateur is not None:
            login(request, utilisateur)
            # succes = redirect a une page en fonction du groupe
            print("connecte")
            return redirect(reverse('referentiel:home'))
        else:
            message = True
    contexte = {'messageErreur': message}
    return render(request, 'utilisateurs/logIn.html', contexte)


def index(request):
    return redirect(reverse('utilisateurs:logIn'))