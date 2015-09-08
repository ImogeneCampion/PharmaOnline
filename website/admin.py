from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Medicament, Pharmacie, Agence, ContactModel

class MedicamentAdmin(admin.ModelAdmin):
   list_display   = ('nom_commercial', 'categorie', 'nom_generique', 'compagnie')
   list_filter    = ('nom_generique','compagnie', 'categorie')
   search_fields  = ('nom_commercial', 'nom_generique')

class PharmacieAdmin(admin.ModelAdmin):
	list_display  = ('nom', 'zone', 'adresse')
	list_filter   = ('zone', 'nom')
	search_fields = ('nom', 'zone')

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('Last_name', 'email', 'msg_subject', 'timestamp')
    list_filter = ('timestamp', 'Last_name', 'msg_subject', 'email')
# Register your models here.
admin.site.register(Medicament, MedicamentAdmin)
admin.site.register(Pharmacie, PharmacieAdmin)
admin.site.register(Agence)
admin.site.register(ContactModel, ContactModelAdmin)
