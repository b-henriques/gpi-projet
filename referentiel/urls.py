from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('creation/', views.creation, name="creation d'article"),
    path('<int:article_id>/', views.detail, name='detail')
]