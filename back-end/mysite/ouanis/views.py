from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import (
    Expediteur, DemandeDeCompteVoyageur, Voyageur, 
    Annonce, DemandeAnnonce, Tag, AnnonceTag, Palier, AnnoncePalier
)
from .serializers import (
    ExpediteurSerializer, DemandeDeCompteVoyageurSerializer, 
    VoyageurSerializer, AnnonceSerializer, DemandeAnnonceSerializer, 
    TagSerializer, AnnonceTagSerializer, PalierSerializer, AnnoncePalierSerializer
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ExpediteurViewSet(viewsets.ModelViewSet):
    queryset = Expediteur.objects.all()
    serializer_class = ExpediteurSerializer
    permission_classes = [IsAuthenticated]

class DemandeDeCompteVoyageurViewSet(viewsets.ModelViewSet):
    queryset = DemandeDeCompteVoyageur.objects.all()
    serializer_class = DemandeDeCompteVoyageurSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        demande = self.get_object()
        demande.est_approuve = True
        demande.save()
        return Response({'status': 'Demande approuvée'}, status=status.HTTP_200_OK)

class VoyageurViewSet(viewsets.ModelViewSet):
    queryset = Voyageur.objects.all()
    serializer_class = VoyageurSerializer
    permission_classes = [IsAuthenticated]

class AnnonceViewSet(viewsets.ModelViewSet):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer
    permission_classes = [IsAuthenticated]

class DemandeAnnonceViewSet(viewsets.ModelViewSet):
    queryset = DemandeAnnonce.objects.all()
    serializer_class = DemandeAnnonceSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        demande = self.get_object()
        demande.statut = 'accepte'
        demande.save()
        return Response({'status': 'Demande acceptée'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        demande = self.get_object()
        demande.statut = 'rejete'
        demande.save()
        return Response({'status': 'Demande rejetée'}, status=status.HTTP_200_OK)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

class AnnonceTagViewSet(viewsets.ModelViewSet):
    queryset = AnnonceTag.objects.all()
    serializer_class = AnnonceTagSerializer
    permission_classes = [IsAuthenticated]

class PalierViewSet(viewsets.ModelViewSet):
    queryset = Palier.objects.all()
    serializer_class = PalierSerializer
    permission_classes = [IsAuthenticated]

class AnnoncePalierViewSet(viewsets.ModelViewSet):
    queryset = AnnoncePalier.objects.all()
    serializer_class = AnnoncePalierSerializer
    permission_classes = [IsAuthenticated]

# Custom view to handle user registration
