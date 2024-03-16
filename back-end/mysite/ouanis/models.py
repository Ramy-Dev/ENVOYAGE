# from django.db import models
# from django.contrib.auth.models import User

# class Utilisateur(models.Model):
#     prenom = models.CharField(max_length=200)
#     nom = models.CharField(max_length=200)
#     age = models.IntegerField()
#     mot_de_passe = models.CharField(max_length=200)  # This should be hashed for security
#     numero_telephone = models.CharField(max_length=200)
#     email = models.EmailField(max_length=254)

#     class Meta:
#         abstract = True

# class Expediteur(Utilisateur):
#     pass

# class Voyageur(Utilisateur):
#     numero_passeport = models.CharField(max_length=200)
#     adresse = models.CharField(max_length=200)
#     date_de_naissance = models.DateField()

# class Annonce(models.Model):
#     createur = models.ForeignKey(Voyageur, on_delete=models.CASCADE)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     lieu_depart = models.CharField(max_length=200)
#     destination = models.CharField(max_length=200)
#     poids_max = models.IntegerField()
#     prix_unit = models.IntegerField()



# class DemandeAnnonce(models.Model):
#     expediteur = models.ForeignKey(Utilisateur, related_name='demandes_expediteur', on_delete=models.CASCADE)
#     destinataire = models.ForeignKey(Utilisateur, related_name='demandes_destinataire', on_delete=models.CASCADE)
#     annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
#     message = models.TextField()
#     STATUT_CHOICES = [
#         ('en_attente', 'En Attente'),
#         ('accepte', 'Accepté'),
#         ('rejete', 'Rejeté')
#     ]
#     statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
#     is_colis = models.BooleanField(default=False)
#     is_courier = models.BooleanField(default=False)
#     date_creation = models.DateTimeField(auto_now_add=True)

#     class DemandeColis(DemandeAnnonce):
#         poids = models.FloatField()

#     class DemandeCourier(DemandeAnnonce):
#         document = models.FileField(upload_to='documents/')
# class DemandeDeCompteVoyageur(models.Model):
#     utilisateur = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     est_approuve = models.BooleanField(default=False)
#     date_de_creation = models.DateTimeField(auto_now_add=True)
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
    # Add fields specific to Expediteur here
    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     verbose_name='groups',
    #     blank=True,
    #     related_name='expediteurs',
    #     related_query_name='expediteur',
    # )

    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     verbose_name='user permissions',
    #     blank=True,
    #     related_name='expediteurs',
    #     related_query_name='expediteur',
    # )
    pass

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
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lieu_depart = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    poids_max = models.IntegerField()
    prix_unit = models.IntegerField()

class DemandeAnnonce(models.Model):
    expediteur = models.ForeignKey(Expediteur, related_name='demandes_expediteur', on_delete=models.CASCADE)
    destinataire = models.ForeignKey(Voyageur, related_name='demandes_destinataire', on_delete=models.CASCADE)
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
    expediteur = models.OneToOneField(Expediteur, on_delete=models.CASCADE, primary_key=True)
    est_approuve = models.BooleanField(default=False)
    date_de_creation = models.DateTimeField(auto_now_add=True)
