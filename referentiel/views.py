from django.shortcuts import render
from .models import Adresse, Catcommerciale, Catprofessionnelle, Individu, Article
from .forms import ArticleForm, IndividuForm


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
        # /test
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
    contexte = { 'articles' : Article.object.all()}
    return render(request, 'referentiel/<Nomfichier>.html', contexte)