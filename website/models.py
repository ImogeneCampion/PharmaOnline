from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pharmacie(models.Model):
	nom       = models.CharField(max_length = 20)
	telephone = models.CharField(max_length = 20)
	adresse   = models.CharField(max_length = 200)
	zone      = models.CharField(max_length = 10, blank=True, null=True)

	def __str__(self):
		return self.nom

class Medicament(models.Model):
	nom_commercial   = models.CharField(max_length = 20) #nom que donne la marque/ la compagnie
	nom_generique    = models.CharField(max_length = 30) #nom scientifique / principe actif
	composition      = models.CharField(max_length = 100) # inactive ingredients/ ingredients secondaires/inactifs
	categorie        = models.CharField(max_length = 50) # utilite usuelle de ce medicament
	forme_gallenique = models.CharField(max_length = 50)
	dosage           = models.CharField(max_length = 100, blank=True, null=True)
	quantite         = models.CharField(max_length = 30)
	compagnie        = models.CharField(max_length = 45)
	Agence           = models.ForeignKey('Agence', blank=True, null=True)
	disponibilite    = models.ManyToManyField(Pharmacie, blank=True, null=True)

	def __str__(self):
		return self.nom_commercial


class Agence(models.Model):
	nom       = models.CharField(max_length = 30)
	adresse   = models.CharField(max_length =100)
	distribue = models.ManyToManyField(Medicament, blank=True, null=True)

	def __str__(self):
		return self.nom


class ContactModel(models.Model):
    first_name  = models.CharField(max_length = 100)
    Last_name   = models.CharField(max_length = 50)
    email       = models.EmailField()
    msg_subject = models.CharField(max_length = 30)
    message     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add = True, auto_now = False)

    def __str__(self):
        return self.email

#class PharmacyProfile(models.Model):
#	user      = models.OneToOneField(User, unique=True)
#	nom       = models.CharField(max_length = 45)
#	adresse   = models.CharField(max_length = 70)
#	telephone = models.PositiveIntegerField()
