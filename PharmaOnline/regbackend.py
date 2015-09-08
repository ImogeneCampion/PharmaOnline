from registration.backends.default.views import RegistrationView
#from website.forms import PharmacyProfileRegistrationForm
#from website.models import PharmacyProfile

class PharmacyRegistrationView(RegistrationView):

    form_class = PharmacyProfileRegistrationForm

    def register(self, request, form_class):
        new_pharmacy = super(PharmacyRegistrationView, self).register(request, form_class)
        pharmacy_profile = PharmacyProfile()
        pharmacy_profile.pharmacy = new_pharmacy
        pharmacy_profile.field = form_class.cleaned_data['field']
        pharmacy_profile.save()
        return pharmacy_profile
