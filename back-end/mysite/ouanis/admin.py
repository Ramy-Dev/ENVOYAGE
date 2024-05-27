from django.contrib import admin
from .models import Utilisateur, Expediteur, Voyageur, Annonce, DemandeAnnonce, DemandeDeCompteVoyageur, Tag, AnnonceTag, Palier, AnnoncePalier


admin.site.register(Expediteur)
admin.site.register(Voyageur)
admin.site.register(Annonce)
admin.site.register(DemandeAnnonce)
admin.site.register(DemandeDeCompteVoyageur)
admin.site.register(Tag)
admin.site.register(AnnonceTag)
admin.site.register(Palier)
admin.site.register(AnnoncePalier)
