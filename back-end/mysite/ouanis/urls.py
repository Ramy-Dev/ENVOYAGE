from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin

from .views import (
    ExpediteurViewSet, DemandeDeCompteVoyageurViewSet, 
    VoyageurViewSet, AnnonceViewSet, DemandeAnnonceViewSet, TagViewSet, 
    AnnonceTagViewSet, PalierViewSet, AnnoncePalierViewSet
)

router = DefaultRouter()
router.register(r'expediteurs', ExpediteurViewSet)
router.register(r'demandes_compte_voyageur', DemandeDeCompteVoyageurViewSet)
router.register(r'voyageurs', VoyageurViewSet)
router.register(r'annonces', AnnonceViewSet)
router.register(r'demandes_annonce', DemandeAnnonceViewSet)
router.register(r'tags', TagViewSet)
router.register(r'annonce_tags', AnnonceTagViewSet)
router.register(r'paliers', PalierViewSet)
router.register(r'annonce_paliers', AnnoncePalierViewSet)

urlpatterns = [
    
    path('', include(router.urls)),
]
