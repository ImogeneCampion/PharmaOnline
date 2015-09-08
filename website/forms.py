from django import forms
from .models import ContactModel
from registration.forms import RegistrationForm

class ContactForm(forms.Form):
	nom = forms.CharField(required = True)
	adresse_mail = forms.EmailField(required = True)
	telephone = forms.CharField(required = False)
	contenu = forms.CharField(
		required = True,
		widget = forms.Textarea
	)

class ContactModelForm(forms.ModelForm):
    class Meta:
        model  = ContactModel
        fields = ['Last_name', 'msg_subject', 'email', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')

        if extension == "edu":
            raise forms.ValidationError("Veuillez rentrer un email acceptable.")
        return email

    def clean_name(self):
        first_name = self.cleaned_data.get(first_name)
        Last_name  = self.cleaned_data.get(Last_name)

        return first_name, Last_name


#class PharmacyProfileRegistrationForm(RegistrationForm):
#	class Meta:
#		model  = PharmacyProfile
#		fields = ("nom", "adresse", "telephone")
