from rest_framework import serializers
from .models import Expediteur, Voyageur, Annonce, DemandeAnnonce, DemandeColis, DemandeCourier, DemandeDeCompteVoyageur

class ExpediteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expediteur
        fields = '__all__'

class VoyageurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voyageur
        fields = '__all__'

class AnnonceSerializer(serializers.ModelSerializer):
    # Include nested fields for createur
    createur_nom = serializers.ReadOnlyField(source='createur.nom')
    createur_prenom = serializers.ReadOnlyField(source='createur.prenom')
    createur_date_de_naissance = serializers.ReadOnlyField(source='createur.date_de_naissance') 
    class Meta:
        model = Annonce
        fields = ['id', 'createur', 'createur_nom','createur_date_de_naissance', 'createur_prenom', 'created_at', 'updated_at', 'lieu_depart', 'destination', 'poids_max', 'prix_unit']

class DemandeAnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeAnnonce
        fields = '__all__'

class DemandeColisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeColis
        fields = '__all__'

class DemandeCourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeCourier
        fields = '__all__'

class DemandeDeCompteVoyageurSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeDeCompteVoyageur
        fields = '__all__'
