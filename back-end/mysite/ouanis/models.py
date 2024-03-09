from django.db import models

class Personne(models.Model):
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    class Meta:
        abstract = True

class Expediteur(Personne):
    pass

class Voyageur(Personne):
    numero_passeport = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    date_de_naissance = models.DateField()

class Annonce(models.Model):
    destination = models.CharField(max_length=200)
    lieu_depart = models.CharField(max_length=200)
    class Meta:
        abstract = True

class AnnonceDeCorier(Annonce):
    poids_max = models.IntegerField()
    
class AnnonceDeColies(Annonce):
    prix_unit = models.IntegerField()

