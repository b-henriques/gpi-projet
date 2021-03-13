from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    message = False
    if 'logIn' in request.POST:
        identifiant = request.POST['identifiant']
        motdepass = request.POST['motdepass']
        utilisateur = authenticate(
            request, username=identifiant, password=motdepass)
        if utilisateur is not None:
            login(request, utilisateur)
            # succes = redirect a une page en fonction du groupe
            return redirect('referentiel/')
        else:
            message = True
    contexte = {'messageErreur': message}
    return render(request, 'utilisateurs/logIn.html', contexte)
