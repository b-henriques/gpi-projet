from django.urls import path

from . import views

app_name = 'publicite'
urlpatterns = [
    path('', views.index, name='home'),
    path('creationCible', views.createCible, name='creationCible')
    #path('creation', views.createPublicite, name='creationPublicite')
]