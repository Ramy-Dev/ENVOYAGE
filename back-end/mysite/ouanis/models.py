from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, MinValueValidator
from django.core.exceptions import ValidationError

# User model with additional fields
class Utilisateur(AbstractUser):
    # Phone number field with validation
    numero_telephone = models.CharField(
        max_length=200, 
        blank=True, 
        null=True, 
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]
    )
    # Address field
    adresse = models.CharField(max_length=200, blank=True, null=True)
    # Date of birth field
    date_de_naissance = models.DateField(blank=True, null=True)
    # Profile picture field
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    # Passport number field
    numero_passeport = models.CharField(max_length=200, blank=True, null=True)
    # Passport photo field
    photos_passeport = models.ImageField(upload_to='passport_images/', blank=True, null=True)
    # Flag indicating if the user is a traveler
    is_voyageur = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # Custom validation for the Utilisateur model
    def clean(self):
        super().clean()
        if self.date_de_naissance and self.date_de_naissance > timezone.now().date():
            raise ValidationError("Date of birth cannot be in the future.")

# Announcement model with additional fields and validations
class Annonce(models.Model):
    # Creator of the announcement
    createur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='annonces')
    # Timestamp when the announcement was created
    created_at = models.DateTimeField(auto_now_add=True)
    # Timestamp when the announcement was last updated
    updated_at = models.DateTimeField(auto_now=True)
    # Departure location
    lieu_depart = models.CharField(max_length=255)
    # Destination location
    destination = models.CharField(max_length=255)
    # Maximum weight allowed with validation
    poids_max = models.FloatField(validators=[MinValueValidator(0.1)])
    # Flag indicating if the announcement is completed
    is_completed = models.BooleanField(default=False)
    # Maximum volume allowed with validation
    volume_max = models.IntegerField(validators=[MinValueValidator(1)])
    # Departure date and time
    date_heure_depart = models.DateTimeField(default=timezone.now)
    # Arrival date and time
    date_heure_arrivee = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Annonce de {self.createur.first_name} {self.createur.last_name} vers {self.destination}"

    # Custom validation for the Annonce model
    def clean(self):
        super().clean()
        if self.date_heure_depart >= self.date_heure_arrivee:
            raise ValidationError("Departure date and time must be before arrival date and time.")

# Request model for announcements with status choices and validation
class DemandeAnnonce(models.Model):
    # Choices for the status field
    STATUT_CHOICES = [
        ('en_attente', 'En Attente'),
        ('accepte', 'Accepté'),
        ('rejete', 'Rejeté')
    ]

    # User making the request
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='demandes_annonce')
    # Related announcement
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='demandes')
    # Status of the request
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    # Timestamp when the request was created
    date_creation = models.DateTimeField(auto_now_add=True)
    # Weight of the requested item with validation
    poids = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.1)])
    # Volume of the requested item with validation
    volume = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.1)])

    def __str__(self):
        return f"Demande de {self.utilisateur.first_name} {self.utilisateur.last_name} pour {self.annonce}"

    # Custom validation for the DemandeAnnonce model
    def clean(self):
        super().clean()
        if self.poids and self.poids < 0:
            raise ValidationError("Weight must be positive.")
        if self.volume and self.volume < 0:
            raise ValidationError("Volume must be positive.")

# Model for travel account requests with validation
class DemandeDeCompteVoyageur(models.Model):
    # User making the request
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='demandes_compte_voyageur')
    # Timestamp when the request was created
    date_de_creation = models.DateTimeField(auto_now_add=True)
    # Passport number
    numero_passeport = models.CharField(max_length=200, blank=True, null=True)
    # Passport photo
    photos_passeport = models.FileField(upload_to='documents/', blank=True, null=True)
    # Address
    adresse = models.CharField(max_length=200, blank=True, null=True)
    # Approval status of the request
    est_approuve = models.BooleanField(default=False)

    def __str__(self):
        return f"Demande de {self.utilisateur.first_name} {self.utilisateur.last_name}"

# Tag model
class Tag(models.Model):
    # Name of the tag
    nom = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nom

# Model for associating tags with announcements
class AnnonceTag(models.Model):
    # Related announcement
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='annonce_tags')
    # Related tag
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tag_annonces')

    def __str__(self):
        return f"{self.annonce} {self.tag}"

# Tier model with validation
class Palier(models.Model):
    # Minimum weight for the tier with validation
    from_poids = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0)])
    # Maximum weight for the tier with validation
    to_poids = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.1)])
    # Price for the tier with validation
    prix = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"Palier from {self.from_poids} to {self.to_poids} priced at {self.prix}"

    # Custom validation for the Palier model
    def clean(self):
        super().clean()
        if self.from_poids and self.to_poids and self.from_poids >= self.to_poids:
            raise ValidationError("from_poids must be less than to_poids.")

# Model for associating tiers with announcements
class AnnoncePalier(models.Model):
    # Related announcement
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='annonce_paliers')
    # Related tier
    palier = models.ForeignKey(Palier, on_delete=models.CASCADE, related_name='palier_annonces')

    def __str__(self):
        return f"{self.annonce} {self.palier}"
