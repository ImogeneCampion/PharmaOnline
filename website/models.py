from django.db import models

# Create your models here.
class Medicament(models.Model):
	nom_commercial = models.CharField(max_length = 20)
	nom_generique = models.CharField(max_length = 30)
	composition = models.CharField(max_length = 100)
	forme_gallenique = models.CharField(max_length = 50)
	dosage = models.CharField(max_length = 100, blank=True, null=True)
	quantite = models.CharField(max_length = 30)
	compagnie = models.CharField(max_length = 15)
	Agence = models.ForeignKey('Agence', blank=True, null=True)
	disponibilite = models.ManyToManyField('Pharmacie', blank=True, null=True)
	
	def __str__(self):
		return self.nom_commercial
	
class Pharmacie(models.Model):
	nom = models.CharField(max_length = 20)
	telephone = models.CharField(max_length = 16)
	adresse = models.CharField(max_length = 200)
	zone = models.CharField(max_length = 10, blank=True, null=True)
	
	def __str__(self):
		return self.nom
		
class Agence(models.Model):
	nom = models.CharField(max_length = 30)
	adresse = models.CharField(max_length =100)
	distrib = models.ManyToManyField('Medicament', blank=True, null=True)
	
	def __str__(self):
		return self.nom