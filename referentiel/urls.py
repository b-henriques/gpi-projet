from django.urls import path

from . import views

app_name = 'referentiel'
urlpatterns = [
    path('', views.index, name='index')
]