from django import forms


class ContactForm(forms.Form):
	nom = forms.CharField(required = True)
	adresse_mail = forms.EmailField(required = True)
	telephone = forms.CharField(required = False)
	contenu = forms.CharField(
		required = True,
		widget = forms.Textarea
	)
	