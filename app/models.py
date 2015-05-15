from django.db import models

# Create your models here.
class Rx(models.Model):
	nom = models.CharField(max_length = 50)
	zone = models.CharField(max_length = 80)
	addresse = models.CharField(max_length = 80)
	telephone = models.TextField(null=True)
	
	def __str__(self):
		return self.nom

class Drug(models.Model):
	pass
	
class Area(models.Model):
	pass