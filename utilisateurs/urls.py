from django.urls import path

from . import views

app_name = 'utilisateurs'
urlpatterns = [
    path('', views.index, name='home'),
    path('logIn', views.logIn, name='logIn'),
    path('logOut', views.logOut, name='logOut'),
]