from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    numero_telephone = models.CharField(max_length=200, blank=True, null=True)
    adresse = models.CharField(max_length=200, blank=True, null=True)
    date_de_naissance = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='%(class)s_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='%(class)s_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        abstract = True

class Expediteur(Utilisateur):
    class Meta:
        verbose_name = "Expediteur"
        verbose_name_plural = "Expediteurs"

class Voyageur(Utilisateur):
    numero_passeport = models.CharField(max_length=200, blank=True, null=True)
    photos_passeport = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Annonce(models.Model):
    createur = models.ForeignKey(Voyageur, on_delete=models.CASCADE, related_name='annonces')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lieu_depart = models.CharField(max_length=200, blank=True, null=True)
    destination = models.CharField(max_length=200)
    poids_max = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Annonce de {self.createur.first_name} {self.createur.last_name} vers {self.destination}"

class DemandeAnnonce(models.Model):
    expediteur = models.ForeignKey(Expediteur, related_name='demandes_expediteur', on_delete=models.CASCADE)
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='demandes')
    STATUT_CHOICES = [
        ('en_attente', 'En Attente'),
        ('accepte', 'Accepté'),
        ('rejete', 'Rejeté')
    ]
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    date_creation = models.DateTimeField(auto_now_add=True)
    poids = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Demande de {self.expediteur.first_name} {self.expediteur.last_name} pour {self.annonce}"

class DemandeDeCompteVoyageur(models.Model):
    expediteur = models.OneToOneField(Expediteur, on_delete=models.CASCADE, primary_key=True)
    date_de_creation = models.DateTimeField(auto_now_add=True)
    numero_passeport = models.CharField(max_length=200, blank=True, null=True)
    photos_passeport = models.FileField(upload_to='documents/', blank=True, null=True)
    adresse = models.CharField(max_length=200, blank=True, null=True)
    est_approuve = models.BooleanField(default=False)

    def __str__(self):
        return f"Demande de {self.expediteur.first_name} {self.expediteur.last_name}"

class Tag(models.Model):
    nom = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.nom}"

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
        return f"{self.nom} {self.prix}"

class AnnoncePalier(models.Model):
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    palier = models.ForeignKey(Palier, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.annonce} {self.palier}"
