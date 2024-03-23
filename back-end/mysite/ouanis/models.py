from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(models.Model):
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    age = models.IntegerField()
    mot_de_passe = models.CharField(max_length=200)  # This should be hashed for security
    numero_telephone = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    class Meta:
        abstract = True

class Expediteur(Utilisateur):
    pass

class DemandeDeCompteVoyageur(models.Model):
    expediteur = models.OneToOneField(Expediteur, on_delete=models.CASCADE, primary_key=True)
    date_de_creation = models.DateTimeField(auto_now_add=True)
    numero_passeport = models.CharField(max_length=200)
    photos_passeport = models.FileField(upload_to='documents/')
    adresse = models.CharField(max_length=200)

class DemandeDeCompteVoyageur(models.Model):
    expediteur = models.OneToOneField(Expediteur, on_delete=models.CASCADE, primary_key=True)
    # est_approuve = models.BooleanField(default=False)
    date_de_creation = models.DateTimeField(auto_now_add=True)
    numero_passeport = models.CharField(max_length=200)
    photos_passeport = models.FileField(upload_to='documents/')
    adresse = models.CharField(max_length=200)


class Voyageur(Utilisateur):
    numero_passeport = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    date_de_naissance = models.DateField()

    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     verbose_name='groups',
    #     blank=True,
    #     related_name='voyageurs',
    #     related_query_name='voyageur',
    # )

    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     verbose_name='user permissions',
    #     blank=True,
    #     related_name='voyageurs',
    #     related_query_name='voyageur',
    # )

class Annonce(models.Model):
    createur = models.ForeignKey(Voyageur, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lieu_depart = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    poids_max = models.IntegerField(blank=True, null=True)
    prix_unit = models.IntegerField(blank=True, null=True)

class DemandeAnnonce(models.Model):
    expediteur = models.ForeignKey(Expediteur, related_name='demandes_expediteur', on_delete=models.CASCADE)
    voyageur = models.ForeignKey(Voyageur, related_name='demandes_destinataire', on_delete=models.CASCADE)
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    message = models.TextField()
    STATUT_CHOICES = [
        ('en_attente', 'En Attente'),
        ('accepte', 'Accepté'),
        ('rejete', 'Rejeté')
    ]
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    date_creation = models.DateTimeField(auto_now_add=True)

class DemandeColis(models.Model):
    demande_annonce = models.OneToOneField(DemandeAnnonce, on_delete=models.CASCADE, primary_key=True)
    poids = models.FloatField()

class DemandeCourier(models.Model):
    demande_annonce = models.OneToOneField(DemandeAnnonce, on_delete=models.CASCADE, primary_key=True)
    document = models.FileField(upload_to='documents/')

class DemandeDeCompteVoyageur(models.Model):
    photos_passeport = models.FileField(upload_to='documents/', default='default_value')  # Specify the default value here
    expediteur = models.OneToOneField(Expediteur, on_delete=models.CASCADE, primary_key=True)
    est_approuve = models.BooleanField(default=False)
    date_de_creation = models.DateTimeField(auto_now_add=True)
