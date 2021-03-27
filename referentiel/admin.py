from django.contrib import admin

from .models import Article, Individu, Catprofessionnelle, Adresse

# Register your models here.
aRegistrer = [Article, Individu, Catprofessionnelle, Adresse]
admin.site.register(aRegistrer)
