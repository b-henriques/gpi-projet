from django.urls import path

from . import views

app_name = 'publicite'
urlpatterns = [
    path('', views.index, name='home'),
    path('creationCible', views.createCible, name='creationCible'),
    path('validateCible', views.validateCible, name='validateCible'),
    path('creationPublicite', views.createPublicite, name='creationPublicite')
]