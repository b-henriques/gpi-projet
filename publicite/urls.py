from django.urls import path

from . import views

app_name = 'Publicite'
urlpatterns = [
    path('', views.index, name='home')
]