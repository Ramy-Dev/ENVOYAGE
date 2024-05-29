from rest_framework import serializers
from .models import (
    Utilisateur, Annonce, DemandeAnnonce,
    DemandeDeCompteVoyageur, Tag, AnnonceTag, Palier, AnnoncePalier
)
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Utilisateur
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)  # Create a token for the new user
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid credentials.")
        else:
            raise serializers.ValidationError("Both username and password are required.")
        
        attrs['user'] = user
        return attrs

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = [
            'id', 'username', 'password', 'first_name', 'last_name', 'email', 'numero_telephone', 
            'adresse', 'date_de_naissance', 'profile_picture', 'numero_passeport', 'photos_passeport', 'is_voyageur'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Utilisateur.objects.create_user(**validated_data)
        return user

class AnnonceSerializer(serializers.ModelSerializer):
    createur = UtilisateurSerializer()

    class Meta:
        model = Annonce
        fields = [
            'id', 'createur', 'created_at', 'updated_at', 'lieu_depart', 
            'destination', 'poids_max'
        ]

    def create(self, validated_data):
        createur_data = validated_data.pop('createur')
        createur = Utilisateur.objects.create(**createur_data)
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
    utilisateur = UtilisateurSerializer()
    annonce = AnnonceSerializer()

    class Meta:
        model = DemandeAnnonce
        fields = [
            'id', 'utilisateur', 'annonce', 'statut', 'date_creation', 'poids'
        ]

    def create(self, validated_data):
        utilisateur_data = validated_data.pop('utilisateur')
        annonce_data = validated_data.pop('annonce')

        utilisateur = Utilisateur.objects.create(**utilisateur_data)
        annonce = Annonce.objects.create(**annonce_data)

        demande_annonce = DemandeAnnonce.objects.create(utilisateur=utilisateur, annonce=annonce, **validated_data)
        return demande_annonce

    def update(self, instance, validated_data):
        utilisateur_data = validated_data.pop('utilisateur')
        annonce_data = validated_data.pop('annonce')

        utilisateur = instance.utilisateur
        annonce = instance.annonce

        instance.statut = validated_data.get('statut', instance.statut)
        instance.poids = validated_data.get('poids', instance.poids)
        instance.save()

        utilisateur.username = utilisateur_data.get('username', utilisateur.username)
        utilisateur.first_name = utilisateur_data.get('first_name', utilisateur.first_name)
        utilisateur.last_name = utilisateur_data.get('last_name', utilisateur.last_name)
        utilisateur.email = utilisateur_data.get('email', utilisateur.email)
        utilisateur.numero_telephone = utilisateur_data.get('numero_telephone', utilisateur.numero_telephone)
        utilisateur.adresse = utilisateur_data.get('adresse', utilisateur.adresse)
        utilisateur.date_de_naissance = utilisateur_data.get('date_de_naissance', utilisateur.date_de_naissance)
        utilisateur.profile_picture = utilisateur_data.get('profile_picture', utilisateur.profile_picture)
        utilisateur.save()

        annonce.createur = annonce_data.get('createur', annonce.createur)
        annonce.created_at = annonce_data.get('created_at', annonce.created_at)
        annonce.updated_at = annonce_data.get('updated_at', annonce.updated_at)
        annonce.lieu_depart = annonce_data.get('lieu_depart', annonce.lieu_depart)
        annonce.destination = annonce_data.get('destination', annonce.destination)
        annonce.poids_max = annonce_data.get('poids_max', annonce.poids_max)
        annonce.save()

        return instance

class DemandeDeCompteVoyageurSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer()

    class Meta:
        model = DemandeDeCompteVoyageur
        fields = [
            'id', 'utilisateur', 'date_de_creation', 'numero_passeport', 
            'photos_passeport', 'adresse', 'est_approuve'
        ]

    def create(self, validated_data):
        utilisateur_data = validated_data.pop('utilisateur')
        utilisateur = Utilisateur.objects.create(**utilisateur_data)
        demande = DemandeDeCompteVoyageur.objects.create(utilisateur=utilisateur, **validated_data)
        return demande

    def update(self, instance, validated_data):
        utilisateur_data = validated_data.pop('utilisateur')
        utilisateur = instance.utilisateur

        instance.numero_passeport = validated_data.get('numero_passeport', instance.numero_passeport)
        instance.photos_passeport = validated_data.get('photos_passeport', instance.photos_passeport)
        instance.adresse = validated_data.get('adresse', instance.adresse)
        instance.est_approuve = validated_data.get('est_approuve', instance.est_approuve)
        instance.save()

        utilisateur.username = utilisateur_data.get('username', utilisateur.username)
        utilisateur.first_name = utilisateur_data.get('first_name', utilisateur.first_name)
        utilisateur.last_name = utilisateur_data.get('last_name', utilisateur.last_name)
        utilisateur.email = utilisateur_data.get('email', utilisateur.email)
        utilisateur.numero_telephone = utilisateur_data.get('numero_telephone', utilisateur.numero_telephone)
        utilisateur.adresse = utilisateur_data.get('adresse', utilisateur.adresse)
        utilisateur.date_de_naissance = utilisateur_data.get('date_de_naissance', utilisateur.date_de_naissance)
        utilisateur.profile_picture = utilisateur_data.get('profile_picture', utilisateur.profile_picture)
        utilisateur.save()

        return instance

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'nom']

class AnnonceTagSerializer(serializers.ModelSerializer):
    annonce = AnnonceSerializer()
    tag = TagSerializer()

    class Meta:
        model = AnnonceTag
        fields = ['id', 'annonce', 'tag']

    def create(self, validated_data):
        annonce_data = validated_data.pop('annonce')
        tag_data = validated_data.pop('tag')

        annonce = Annonce.objects.create(**annonce_data)
        tag = Tag.objects.create(**tag_data)

        annonce_tag = AnnonceTag.objects.create(annonce=annonce, tag=tag, **validated_data)
        return annonce_tag

    def update(self, instance, validated_data):
        annonce_data = validated_data.pop('annonce')
        tag_data = validated_data.pop('tag')

        annonce = instance.annonce
        tag = instance.tag

        instance.save()

        annonce.createur = annonce_data.get('createur', annonce.createur)
        annonce.created_at = annonce_data.get('created_at', annonce.created_at)
        annonce.updated_at = annonce_data.get('updated_at', annonce.updated_at)
        annonce.lieu_depart = annonce_data.get('lieu_depart', annonce.lieu_depart)
        annonce.destination = annonce_data.get('destination', annonce.destination)
        annonce.poids_max = annonce_data.get('poids_max', annonce.poids_max)
        annonce.save()

        tag.nom = tag_data.get('nom', tag.nom)
        tag.save()

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
