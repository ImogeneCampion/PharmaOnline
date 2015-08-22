from django.contrib import admin
from .models import Medicament, Pharmacie, Agence

class MedicamentAdmin(admin.ModelAdmin):
   list_display   = ('nom_commercial', 'categorie', 'nom_generique', 'compagnie')
   list_filter    = ('nom_generique','compagnie', 'categorie')
   search_fields  = ('nom_commercial', 'nom_generique')

class PharmacieAdmin(admin.ModelAdmin):
	list_display  = ('nom', 'zone', 'adresse')
	list_filter   = ('zone', 'nom')
	search_fields = ('nom', 'zone')

# Register your models here.
admin.site.register(Medicament, MedicamentAdmin)
admin.site.register(Pharmacie, PharmacieAdmin)
admin.site.register(Agence)
