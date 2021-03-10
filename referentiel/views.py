from django.shortcuts import render

from django.http import HttpResponse

#page admin ref
def index(request):
    return HttpResponse("page ref.")

#page detail article
def detail(request, article_id):
    return HttpResponse("informations aricle %s." % article_id)

#page creation article
def creation(request):
    return render(request, "referentiel/createArticle.html")

#page creation individu

