from django.contrib import admin
from .models import Utilisateur, Expediteur, Voyageur, Annonce, DemandeAnnonce, DemandeColis, DemandeCourier, DemandeDeCompteVoyageur

admin.site.register(Expediteur)
admin.site.register(Voyageur)
admin.site.register(Annonce)
admin.site.register(DemandeAnnonce)
admin.site.register(DemandeColis)
admin.site.register(DemandeCourier)
admin.site.register(DemandeDeCompteVoyageur)
