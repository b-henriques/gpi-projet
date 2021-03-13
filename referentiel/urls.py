from django.urls import path

from . import views

app_name = 'referentiel'
urlpatterns = [
    path('', views.index, name='home'),
    path('creation', views.creationReferentiel, name='creationReferentiel'),
    path('articles', views.tableArticle, name='affichageReferentielArticles'),
    path('individus', views.tableIndividu, name='affichageReferentielIndividus'),
    path('delarticle/<str:pk>', views.delArticle, name='supressionArticle'),
    path('delindividu/<str:pk>', views.delIndividu, name='supressionIndividu')
]