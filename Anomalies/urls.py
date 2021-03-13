from django.urls import path

from . import views

app_name = 'Anomalies'
urlpatterns = [
    path('', views.index, name='home')
]