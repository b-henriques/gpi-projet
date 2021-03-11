from django.contrib import admin

from .models import Article, Individu, Catcommerciale, Catprofessionnelle, Adresse

# Register your models here.
aRegistrer = [Article, Individu, Catprofessionnelle, Catcommerciale, Adresse]
admin.site.register(aRegistrer)
