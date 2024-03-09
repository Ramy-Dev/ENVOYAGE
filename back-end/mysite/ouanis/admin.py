from django.contrib import admin

# Register your models here.

from .models import Expediteur,Voyageur,AnnonceDeCorier,AnnonceDeColies
admin.site.register(Voyageur)
admin.site.register(Expediteur)
admin.site.register(AnnonceDeCorier)
admin.site.register(AnnonceDeColies)
