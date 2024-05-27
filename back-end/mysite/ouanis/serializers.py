from rest_framework import serializers
from .models import (
    Expediteur, DemandeDeCompteVoyageur, Voyageur, 
    Annonce, DemandeAnnonce, Tag, AnnonceTag, Palier, AnnoncePalier
)


class ExpediteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expediteur
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'numero_telephone', 
            'adresse', 'date_de_naissance', 'profile_picture'
        ]

class DemandeDeCompteVoyageurSerializer(serializers.ModelSerializer):
    expediteur = ExpediteurSerializer()

    class Meta:
        model = DemandeDeCompteVoyageur
        fields = [
            'expediteur', 'date_de_creation', 'numero_passeport', 
            'photos_passeport', 'adresse', 'est_approuve'
        ]

    def create(self, validated_data):
        expediteur_data = validated_data.pop('expediteur')
        expediteur = Expediteur.objects.create(**expediteur_data)
        demande = DemandeDeCompteVoyageur.objects.create(expediteur=expediteur, **validated_data)
        return demande

    def update(self, instance, validated_data):
        expediteur_data = validated_data.pop('expediteur')
        expediteur = instance.expediteur

        instance.numero_passeport = validated_data.get('numero_passeport', instance.numero_passeport)
        instance.photos_passeport = validated_data.get('photos_passeport', instance.photos_passeport)
        instance.adresse = validated_data.get('adresse', instance.adresse)
        instance.est_approuve = validated_data.get('est_approuve', instance.est_approuve)
        instance.save()

        expediteur.username = expediteur_data.get('username', expediteur.username)
        expediteur.first_name = expediteur_data.get('first_name', expediteur.first_name)
        expediteur.last_name = expediteur_data.get('last_name', expediteur.last_name)
        expediteur.email = expediteur_data.get('email', expediteur.email)
        expediteur.numero_telephone = expediteur_data.get('numero_telephone', expediteur.numero_telephone)
        expediteur.adresse = expediteur_data.get('adresse', expediteur.adresse)
        expediteur.date_de_naissance = expediteur_data.get('date_de_naissance', expediteur.date_de_naissance)
        expediteur.profile_picture = expediteur_data.get('profile_picture', expediteur.profile_picture)
        expediteur.save()

        return instance

class VoyageurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voyageur
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'numero_telephone', 
            'adresse', 'date_de_naissance', 'profile_picture', 'numero_passeport', 'photos_passeport'
        ]

class AnnonceSerializer(serializers.ModelSerializer):
    createur = VoyageurSerializer()

    class Meta:
        model = Annonce
        fields = [
            'id', 'createur', 'created_at', 'updated_at', 'lieu_depart', 
            'destination', 'poids_max'
        ]

    def create(self, validated_data):
        createur_data = validated_data.pop('createur')
        createur = Voyageur.objects.create(**createur_data)
        annonce = Annonce.objects.create(createur=createur, **validated_data)
        return annonce

    def update(self, instance, validated_data):
        createur_data = validated_data.pop('createur')
        createur = instance.createur

        instance.lieu_depart = validated_data.get('lieu_depart', instance.lieu_depart)
        instance.destination = validated_data.get('destination', instance.destination)
        instance.poids_max = validated_data.get('poids_max', instance.poids_max)
        instance.save()

        createur.username = createur_data.get('username', createur.username)
        createur.first_name = createur_data.get('first_name', createur.first_name)
        createur.last_name = createur_data.get('last_name', createur.last_name)
        createur.email = createur_data.get('email', createur.email)
        createur.numero_telephone = createur_data.get('numero_telephone', createur.numero_telephone)
        createur.adresse = createur_data.get('adresse', createur.adresse)
        createur.date_de_naissance = createur_data.get('date_de_naissance', createur.date_de_naissance)
        createur.profile_picture = createur_data.get('profile_picture', createur.profile_picture)
        createur.numero_passeport = createur_data.get('numero_passeport', createur.numero_passeport)
        createur.photos_passeport = createur_data.get('photos_passeport', createur.photos_passeport)
        createur.save()

        return instance

class DemandeAnnonceSerializer(serializers.ModelSerializer):
    expediteur = ExpediteurSerializer()
    annonce = AnnonceSerializer()

    class Meta:
        model = DemandeAnnonce
        fields = [
            'id', 'expediteur', 'annonce', 'statut', 'date_creation', 'poids'
        ]

    def create(self, validated_data):
        expediteur_data = validated_data.pop('expediteur')
        annonce_data = validated_data.pop('annonce')

        expediteur = Expediteur.objects.create(**expediteur_data)
        annonce = Annonce.objects.create(**annonce_data)

        demande_annonce = DemandeAnnonce.objects.create(expediteur=expediteur, annonce=annonce, **validated_data)
        return demande_annonce

    def update(self, instance, validated_data):
        expediteur_data = validated_data.pop('expediteur')
        annonce_data = validated_data.pop('annonce')

        expediteur = instance.expediteur
        annonce = instance.annonce

        instance.statut = validated_data.get('statut', instance.statut)
        instance.poids = validated_data.get('poids', instance.poids)
        instance.save()

        expediteur.username = expediteur_data.get('username', expediteur.username)
        expediteur.first_name = expediteur_data.get('first_name', expediteur.first_name)
        expediteur.last_name = expediteur_data.get('last_name', expediteur.last_name)
        expediteur.email = expediteur_data.get('email', expediteur.email)
        expediteur.numero_telephone = expediteur_data.get('numero_telephone', expediteur.numero_telephone)
        expediteur.adresse = expediteur_data.get('adresse', expediteur.adresse)
        expediteur.date_de_naissance = expediteur_data.get('date_de_naissance', expediteur.date_de_naissance)
        expediteur.profile_picture = expediteur_data.get('profile_picture', expediteur.profile_picture)
        expediteur.save()

        annonce.createur = annonce_data.get('createur', annonce.createur)
        annonce.created_at = annonce_data.get('created_at', annonce.created_at)
        annonce.updated_at = annonce_data.get('updated_at', annonce.updated_at)
        annonce.lieu_depart = annonce_data.get('lieu_depart', annonce.lieu_depart)
        annonce.destination = annonce_data.get('destination', annonce.destination)
        annonce.poids_max = annonce_data.get('poids_max', annonce.poids_max)
        annonce.save()

        return instance

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'nom']

class AnnonceTagSerializer(serializers.ModelSerializer):
    annonce = AnnonceSerializer()
    Tag = TagSerializer()

    class Meta:
        model = AnnonceTag
        fields = ['id', 'annonce', 'Tag']

    def create(self, validated_data):
        annonce_data = validated_data.pop('annonce')
        Tag_data = validated_data.pop('Tag')

        annonce = Annonce.objects.create(**annonce_data)
        Tag = Tag.objects.create(**Tag_data)

        annonce_Tag = AnnonceTag.objects.create(annonce=annonce, Tag=Tag, **validated_data)
        return annonce_Tag

    def update(self, instance, validated_data):
        annonce_data = validated_data.pop('annonce')
        Tag_data = validated_data.pop('Tag')

        annonce = instance.annonce
        Tag = instance.Tag

        instance.save()

        annonce.createur = annonce_data.get('createur', annonce.createur)
        annonce.created_at = annonce_data.get('created_at', annonce.created_at)
        annonce.updated_at = annonce_data.get('updated_at', annonce.updated_at)
        annonce.lieu_depart = annonce_data.get('lieu_depart', annonce.lieu_depart)
        annonce.destination = annonce_data.get('destination', annonce.destination)
        annonce.poids_max = annonce_data.get('poids_max', annonce.poids_max)
        annonce.save()

        Tag.nom = Tag_data.get('nom', Tag.nom)
        Tag.save()

        return instance

class PalierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palier
        fields = ['id', 'from_poids', 'to_poids', 'prix']

class AnnoncePalierSerializer(serializers.ModelSerializer):
    annonce = AnnonceSerializer()
    palier = PalierSerializer()

    class Meta:
        model = AnnoncePalier
        fields = ['id', 'annonce', 'palier']

    def create(self, validated_data):
        annonce_data = validated_data.pop('annonce')
        palier_data = validated_data.pop('palier')

        annonce = Annonce.objects.create(**annonce_data)
        palier = Palier.objects.create(**palier_data)

        annonce_palier = AnnoncePalier.objects.create(annonce=annonce, palier=palier, **validated_data)
        return annonce_palier

    def update(self, instance, validated_data):
        annonce_data = validated_data.pop('annonce')
        palier_data = validated_data.pop('palier')

        annonce = instance.annonce
        palier = instance.palier

        instance.save()

        annonce.createur = annonce_data.get('createur', annonce.createur)
        annonce.created_at = annonce_data.get('created_at', annonce.created_at)
        annonce.updated_at = annonce_data.get('updated_at', annonce.updated_at)
        annonce.lieu_depart = annonce_data.get('lieu_depart', annonce.lieu_depart)
        annonce.destination = annonce_data.get('destination', annonce.destination)
        annonce.poids_max = annonce_data.get('poids_max', annonce.poids_max)
        annonce.save()

        palier.from_poids = palier_data.get('from_poids', palier.from_poids)
        palier.to_poids = palier_data.get('to_poids', palier.to_poids)
        palier.prix = palier_data.get('prix', palier.prix)
        palier.save()

        return instance
