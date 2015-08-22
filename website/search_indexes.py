from haystack import indexes
from .models import Medicament, Pharmacie

class MedicamentIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	nom_comm = indexes.CharField(model_attr='nom_commercial')
	nom_gen = indexes.CharField(model_attr='nom_generique')
	comp = indexes.CharField(model_attr='compagnie')

	def get_model(self):
		return Medicament

class PharmacieIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	nom = indexes.CharField(model_attr='nom')
	adresse = indexes.CharField(model_attr='adresse')
	zone = indexes.CharField(model_attr='zone')

	def get_model(self):
		return Pharmacie
