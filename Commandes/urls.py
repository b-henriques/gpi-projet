from django.urls import path

from . import views

app_name = 'commandes'
urlpatterns = [
    path('', views.index, name='home'),
    path('createCommandeIndividu', views.createCommandeIndividu, name='createCommandeIndividu')
]