from django.db import models

# Create your models here.


class Article(models.Model):
    designation = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=6, decimal_places=2)


class catprofessionnelle(models.Model):
    nom = models.CharField(max_length=100)


class catcommerciale(models.Model):
    nom = models.CharField(max_length=100)


class Adresse(models.Model):
    numero = models.IntegerField()
    rue = models.CharField(max_length=100)
    codepostal = models.IntegerField(max_length=5)
    ville = models.CharField(max_length=50)


class Individu(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    datenaissance = models.DateField()
    ntel = models.IntegerField(max_length=10)
    mail = models.EmailField()
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    adresse = models.ForeignKey(catprofessionnelle, on_delete=models.CASCADE)
