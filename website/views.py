from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Pharmacie
from .forms import ContactForm

# Create your views here.
def home(request):
	if request.user.is_authenticated() and request.user.is_staff:
		queryset = Users.objects.all()
		context = {
		"queryset": queryset,
		}
	return render(request, 'website/base.html', context)

def pharmacies(request):
	pharma = Pharmacie.objects.all()
	paginator = Paginator(pharma, 5)
	page = request.GET.get('page')
	try:
		pharmacies = paginator.page(page)
	except PageNotAnInteger:
		pharmacie = paginator.page(1)
	except EmptyPage:
		pharmacies = paginator.page(paginator.num_pages)

	return render_to_response('website/pharmacies.html', {'pharmacies': pharma})

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		for key, value in form.cleaned_data.items():
			print (key, value)
			#print form.cleaned_data.get(key)
		full_name = form.cleaned_data.get("Nom")
		email = form.cleaned_data.get("Adresse_email: ")
		message = form.cleaned_data.get("Contenu: ")

	context = {
		"form": form,
	}
	return render(request, "website/contact.html", context)
