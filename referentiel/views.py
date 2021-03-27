from django.shortcuts import get_object_or_404, render, redirect
from .models import Adresse, Catprofessionnelle, Individu, Article
from .forms import ArticleForm, IndividuForm
from django.http.response import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.urls import reverse

# TODO: possibilite de creer cat pro en meme temps que Ind
# TODO: modification Art ou Ind

# @permission_required('perm_administrerRef')


def index(request):
    return render(request, 'referentiel/referentiel_view.html')


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
        print(True)
        # affiche les donnees du formulaire
        # print(form2.cleaned_data)

        # creer adress
        adresse = Adresse(
            numero=form2.cleaned_data['numero'],
            rue=form2.cleaned_data['rue'],
            codepostal=form2.cleaned_data['codepostal'],
            ville=form2.cleaned_data['ville']
        )
        adresse.save()
        individu = Individu(
            nom=form2.cleaned_data['nom'],
            prenom=form2.cleaned_data['prenom'],
            datenaissance=form2.cleaned_data['datenaissance'],
            ntel=form2.cleaned_data['ntel'],
            mail=form2.cleaned_data['mail'],
            adresse=adresse,
            catcommerciale=form2.cleaned_data['catcommerciale'],
            catprofessionnelle=form2.cleaned_data['catprofessionnelle'],
        )
        individu.save()

    context = {'form': ArticleForm(), 'formInd': IndividuForm()}
    return render(request, 'referentiel/createForm.html', context)


def tableArticle(request):
    contexte = {'articles': Article.objects.all()}
    return render(request, 'referentiel/afficheArticle.html', contexte)


def tableIndividu(request):
    contexte = {'individus': Individu.objects.all()}
    return render(request, 'referentiel/afficheIndividu.html', contexte)


def delArticle(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if(request.method == "POST"):
        if "annuler" in request.POST:
            return redirect('/referentiel/articles')
        else:
            article.delete()
            return redirect('/referentiel/articles')
    contexte = {'article': article}
    return render(request, 'referentiel/deletearticle.html', contexte)


def delIndividu(request, pk):
    individu = get_object_or_404(Individu, pk=pk)
    if(request.method == "POST"):
        if "annuler" in request.POST:
            return redirect('/referentiel/individus')
        else:
            individu.delete()
            return redirect('/referentiel/individus')
    contexte = {'individu': individu}
    return render(request, 'referentiel/deleteindividu.html', contexte)


def modifierArticle(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect(reverse("referentiel:affichageReferentielArticles"))
    contexte = {'form': form}
    return render(request, 'referentiel/modifArticle.html', contexte)


def modifierIndividu(request, pk):
    individu = get_object_or_404(Individu, pk=pk)
    form = IndividuForm(request.POST or None, initial={
        'nom' : individu.nom,
        'prenom' : individu.prenom,
        'datenaissance' : individu.datenaissance,
        'ntel' : individu.ntel,
        'mail' : individu.mail,
        'catcommerciale' : individu.catcommerciale,
        'catprofessionnelle' : individu.catprofessionnelle,
        'numero' : individu.adresse.numero,
        'rue' : individu.adresse.rue,
        'codepostal' : individu.adresse.codepostal,
        'ville' : individu.adresse.ville 
    })
    if form.is_valid():
        adresse = individu.adresse
        adresse.numero=form.cleaned_data['numero']
        adresse.rue=form.cleaned_data['rue']
        adresse.codepostal=form.cleaned_data['codepostal']
        adresse.ville=form.cleaned_data['ville']
        adresse.save()
        individu.nom=form.cleaned_data['nom']
        individu.prenom=form.cleaned_data['prenom']
        individu.datenaissance=form.cleaned_data['datenaissance']
        individu.ntel=form.cleaned_data['ntel']
        individu.mail=form.cleaned_data['mail']
        individu.adresse=adresse
        individu.catcommerciale=form.cleaned_data['catcommerciale']
        individu.catprofessionnelle=form.cleaned_data['catprofessionnelle']
        individu.save()
        return redirect(reverse("referentiel:affichageReferentielIndividus"))
    contexte = {'form': form, 'id':pk}
    return render(request, 'referentiel/modifIndividu.html', contexte)
