from django.urls import path

from . import views

app_name = 'anomalies'
urlpatterns = [
    path('', views.index, name='home'),
    path('afficheAnomalies', views.afficheAnomalies, name='afficheAnomalies'),
    path('autresAnomalies/<str:pk>', views.autresAnomalies, name='autresAnomalies'),
    path('courrier/<str:pk>', views.envoiCourrier, name='envoiCourrier')
]