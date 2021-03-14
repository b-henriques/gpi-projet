from django.shortcuts import get_object_or_404, render, redirect
from .models import Adresse, Catcommerciale, Catprofessionnelle, Individu, Article
from .forms import ArticleForm, IndividuForm
from django.http.response import HttpResponse
from django.contrib.auth.decorators import permission_required

#TODO: possibilite de creer cat pro en meme temps que Ind
#TODO: modification Art ou Ind

@permission_required('perm_administrerRef')
def index(request):
    return HttpResponse("<h1> Referentiel </h1>")

def creationReferentiel(request):
    # affiche le cde html de form
    # print(form)
    form2 = IndividuForm(request.POST or None)

    if ("article" in request.POST):
        form = ArticleForm(request.POST or None)
        if form.is_valid():
            form.save()
            # affiche la val d'un champ form.cleaned_data['nom-champ']

    if form2.is_valid():
        # affiche les donnees du formulaire
        #print(form2.cleaned_data)

        # creer adress
        adresse = Adresse(
            numero=form2.cleaned_data['numero'],
            rue=form2.cleaned_data['rue'],
            codepostal=form2.cleaned_data['codepostal'],
            ville=form2.cleaned_data['ville']
        )
        adresse.save()
        individu = Individu(
            nom= form2.cleaned_data['nom'],
            prenom = form2.cleaned_data['prenom'],
            datenaissance = form2.cleaned_data['datenaissance'],
            ntel = form2.cleaned_data['ntel'],
            mail = form2.cleaned_data['mail'],
            adresse = adresse,
            catcommerciale = form2.cleaned_data['catcommerciale'],
            catprofessionnelle = form2.cleaned_data['catprofessionnelle'],
        )
        individu.save()

    context = {'form': ArticleForm(), 'formInd': IndividuForm()}
    return render(request, 'referentiel/createForm.html', context)


def tableArticle(request):
    contexte = { 'articles' : Article.objects.all()}
    return render(request, 'referentiel/afficheArticle.html', contexte)

def tableIndividu(request):
    contexte = { 'individus' : Individu.objects.all()}
    return render(request, 'referentiel/afficheIndividu.html', contexte)

def delArticle(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if(request.method == "POST"):
        if "annuler" in request.POST:
            return redirect('/referentiel/articles')
        else:
            article.delete()
            return redirect('/referentiel/creation')
    contexte = { 'article' : article}
    return render(request, 'referentiel/deletearticle.html', contexte)

def delIndividu(request, pk):
    individu = get_object_or_404(Individu, pk=pk)
    if(request.method == "POST"):
        if "annuler" in request.POST:
            return redirect('/referentiel/creation')
        else:
            individu.delete()
            return redirect('/referentiel/creation')
    contexte = { 'individu' : individu}
    return render(request, 'referentiel/deleteindividu.html', contexte)