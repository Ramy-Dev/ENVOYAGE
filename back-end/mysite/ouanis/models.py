from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class Utilisateur(AbstractUser):
    numero_telephone = models.CharField(max_length=200, blank=True, null=True)
    adresse = models.CharField(max_length=200, blank=True, null=True)
    date_de_naissance = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    numero_passeport = models.CharField(max_length=200, blank=True, null=True)
    photos_passeport = models.FileField(upload_to='documents/', blank=True, null=True)
    is_voyageur = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Annonce(models.Model):
    createur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lieu_depart = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    poids_max = models.FloatField()
    volume_max = models.IntegerField()
    date_heure_depart = models.DateTimeField(default=timezone.now)
    date_heure_arrivee = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Annonce de {self.createur.first_name} {self.createur.last_name} vers {self.destination}"

class DemandeAnnonce(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En Attente'),
        ('accepte', 'Accepté'),
        ('rejete', 'Rejeté')
    ]

    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='demandes')
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    date_creation = models.DateTimeField(auto_now_add=True)
    poids = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Demande de {self.utilisateur.first_name} {self.utilisateur.last_name} pour {self.annonce}"

class DemandeDeCompteVoyageur(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_de_creation = models.DateTimeField(auto_now_add=True)
    numero_passeport = models.CharField(max_length=200, blank=True, null=True)
    photos_passeport = models.FileField(upload_to='documents/', blank=True, null=True)
    adresse = models.CharField(max_length=200, blank=True, null=True)
    est_approuve = models.BooleanField(default=False)

    def __str__(self):
        return f"Demande de {self.utilisateur.first_name} {self.utilisateur.last_name}"

class Tag(models.Model):
    nom = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nom

class AnnonceTag(models.Model):
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.annonce} {self.tag}"

class Palier(models.Model):
    from_poids = models.FloatField(blank=True, null=True)
    to_poids = models.FloatField(blank=True, null=True)
    prix = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} {self.prix}"

class AnnoncePalier(models.Model):
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    palier = models.ForeignKey(Palier, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.annonce} {self.palier}"
