from django.urls import path

from . import views

app_name = 'referentiel'
urlpatterns = [
    path('', views.index, name='index'),
    path('affiche_article', views.affiche_article, name='affiche_article')
]