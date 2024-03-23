from rest_framework import viewsets,permissions
from .models import  Expediteur, Voyageur, Annonce, DemandeAnnonce, DemandeColis, DemandeCourier, DemandeDeCompteVoyageur
from .serializers import  ExpediteurSerializer, VoyageurSerializer, AnnonceSerializer, DemandeAnnonceSerializer, DemandeColisSerializer, DemandeCourierSerializer, DemandeDeCompteVoyageurSerializer


class ExpediteurViewSet(viewsets.ModelViewSet):
    queryset = Expediteur.objects.all()
    serializer_class = ExpediteurSerializer

class VoyageurViewSet(viewsets.ModelViewSet):
    queryset = Voyageur.objects.all()
    serializer_class = VoyageurSerializer

class AnnonceViewSet(viewsets.ModelViewSet):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer
    permission_classes = [permissions.AllowAny]

class DemandeAnnonceViewSet(viewsets.ModelViewSet):
    queryset = DemandeAnnonce.objects.all()
    serializer_class = DemandeAnnonceSerializer

class DemandeColisViewSet(viewsets.ModelViewSet):
    queryset = DemandeColis.objects.all()
    serializer_class = DemandeColisSerializer

class DemandeCourierViewSet(viewsets.ModelViewSet):
    queryset = DemandeCourier.objects.all()
    serializer_class = DemandeCourierSerializer

class DemandeDeCompteVoyageurViewSet(viewsets.ModelViewSet):
    queryset = DemandeDeCompteVoyageur.objects.all()
    serializer_class = DemandeDeCompteVoyageurSerializer
