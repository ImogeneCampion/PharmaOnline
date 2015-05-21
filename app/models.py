from django.db import models

# Create your models here.
class Rx(models.Model):
	nom = models.CharField(max_length = 50)
	zone = models.CharField(max_length = 80)
	adresse = models.CharField(max_length = 80)
	telephone = models.TextField(null=True)
	
	def __str__(self):
		return self.nom

class Drug(models.Model):
	nom = models.CharField(max_length = 50)
	famille_molecule = models.CharField(max_length = 50)
	posologie = models.TextField(null = True)
	nom_populaire = models.TextField(null=True)
	
	def __str__(self):
		return self.nom