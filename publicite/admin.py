from django.contrib import admin

from .models import Cible, Publicite

# Register your models here.
aPublicite = [Publicite, Cible]
admin.site.register(aPublicite)