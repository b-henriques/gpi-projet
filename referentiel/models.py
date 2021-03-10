from django.db import models

# Create your models here.


class Article(models.Model):
    designation = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return self.designation


class Catprofessionnelle(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nom


class Catcommerciale(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nom


class Adresse(models.Model):
    numero = models.IntegerField()
    rue = models.CharField(max_length=100)
    codepostal = models.DecimalField(max_digits=5, decimal_places=0)
    ville = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.numero)+self.rue+"\n"+str(self.codepostal)+self.ville


class Individu(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    datenaissance = models.DateField()
    ntel = models.DecimalField(max_digits=10, decimal_places=0)
    mail = models.EmailField(null=True)
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    catprofessionnelle = models.ForeignKey(Catprofessionnelle, on_delete=models.CASCADE)
    catcommerciale = models.ForeignKey(Catcommerciale, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "(id = "+str(self.id)+", nom= "+self.nom+", prenom= "+self.prenom
