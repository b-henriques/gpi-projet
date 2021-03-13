from django.urls import path

from . import views

app_name = 'referentiel'
urlpatterns = [
    path('creation', views.creationReferentiel, name='creationReferentiel'),
    path('articles', views.tableArticle, name='affichageReferentiel')
]