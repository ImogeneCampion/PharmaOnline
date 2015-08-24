from django import forms
from .models import Medicament


class ContactForm(forms.Form):
	nom = forms.CharField(required = True)
	adresse_mail = forms.EmailField(required = True)
	telephone = forms.CharField(required = False)
	contenu = forms.CharField(
		required = True,
		widget = forms.Textarea
	)


class MedicamentForm(forms.ModelForm):
	pass
