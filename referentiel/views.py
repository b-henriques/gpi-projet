from django.shortcuts import render

def index(request):
    return render(request, 'referentiel/createArticle.html', {})

def affiche_article(request):
    return render(request, 'referentiel/afficheArticle.html', {})
