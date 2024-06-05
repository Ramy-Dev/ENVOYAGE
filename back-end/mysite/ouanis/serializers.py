from rest_framework import serializers
from .models import (
    Utilisateur, Annonce, DemandeAnnonce,
    DemandeDeCompteVoyageur, Tag, AnnonceTag, Palier, AnnoncePalier
)
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
        user = Utilisateur.objects.create_user(**validated_data)
        Token.objects.create(user=user)
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

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PalierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palier
        fields = ['id', 'from_poids', 'to_poids', 'prix']

class AnnonceTagSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = AnnonceTag
        fields = ['id', 'tag']

class AnnoncePalierSerializer(serializers.ModelSerializer):
    palier = PalierSerializer()

    class Meta:
        model = AnnoncePalier
        fields = ['id', 'palier']

class AnnonceSerializer(serializers.ModelSerializer):
    createur = serializers.PrimaryKeyRelatedField(queryset=Utilisateur.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), write_only=True)
    paliers = AnnoncePalierSerializer(many=True, write_only=True)

    class Meta:
        model = Annonce
        fields = [
            'id', 'createur', 'created_at', 'updated_at', 'lieu_depart', 
            'destination', 'poids_max', 'volume_max', 'date_heure_depart', 'date_heure_arrivee', 'tags', 'paliers'
        ]

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        paliers_data = validated_data.pop('paliers')
        annonce = Annonce.objects.create(**validated_data)

        for tag in tags_data:
            AnnonceTag.objects.create(annonce=annonce, tag=tag)

        for palier_data in paliers_data:
            palier = Palier.objects.create(**palier_data)
            AnnoncePalier.objects.create(annonce=annonce, palier=palier)

        return annonce
    
    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        paliers_data = validated_data.pop('paliers', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if tags_data:
            instance.tags.clear()
            for tag in tags_data:
                AnnonceTag.objects.create(annonce=instance, tag=tag)

        if paliers_data:
            instance.paliers.clear()
            for palier_data in paliers_data:
                palier = Palier.objects.create(**palier_data)
                AnnoncePalier.objects.create(annonce=instance, palier=palier)

        instance.save()
        return instance

class DemandeAnnonceSerializer(serializers.ModelSerializer):
    utilisateur = serializers.PrimaryKeyRelatedField(queryset=Utilisateur.objects.all())
    annonce = serializers.PrimaryKeyRelatedField(queryset=Annonce.objects.all())

    class Meta:
        model = DemandeAnnonce
        fields = ['id', 'utilisateur', 'annonce', 'statut', 'date_creation', 'poids', 'volume']

    def create(self, validated_data):
        return DemandeAnnonce.objects.create(**validated_data)

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
        utilisateur_data = validated_data.pop('utilisateur', None)
        if utilisateur_data:
            UtilisateurSerializer().update(instance.utilisateur, utilisateur_data)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs
