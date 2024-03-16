from rest_framework import serializers
from .models import  Expediteur, Voyageur, Annonce, DemandeAnnonce, DemandeColis, DemandeCourier, DemandeDeCompteVoyageur

class ExpediteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expediteur
        fields = '__all__'

class VoyageurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voyageur
        fields = '__all__'

class AnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annonce
        fields = '__all__'

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
