from django.urls import path

from . import views

app_name = 'commandes'
urlpatterns = [
    path('', views.index, name='home'),
    path('createCommandeIndividu', views.createCommandeIndividu, name='createCommandeIndividu'),
    path('createCommandeIndividuNouveau', views.createCommandeIndividuNouveau, name='createCommandeIndividuNouveau'),
    path('createCommandeArticle/<str:pk>', views.createCommandeArticle, name='createCommandeArticle'),
    path('createCommandeReglementChoix/<str:pk>', views.createCommandeReglementChoix, name='createCommandeReglementChoix'),
    path('createCommandeReglementCarte/<str:pk>', views.createCommandeReglementCarte, name='createCommandeReglementCarte'),
    path('createCommandeReglementCheque/<str:pk>', views.createCommandeReglementCheque, name='createCommandeReglementCheque'),
    path('createCommandeRecap/<str:pk>', views.commandeRecap, name='createCommandeRecap'),
    path('validiteCommande/<str:pk>', views.validiteCommande, name='validiteCommande'),
    path('reponseValiditeCommande/<str:pk>', views.reponseValiditeCommande, name='reponseValiditeCommande')
]