from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("page ref.")


def detail(request, article_id):
    return HttpResponse("You're looking at question %s." % article_id)

def results(request, article_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % article_id)
