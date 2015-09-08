from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Pharmacie, ContactModel
from .forms import ContactForm, ContactModelForm

# Create your views here.
def home(request):
	if request.user.is_authenticated() and request.user.is_staff:
		queryset = Users.objects.all()
		context = {
		"queryset": queryset,
		}
	return render(request, 'website/base.html', context)

def pharmacies_list(request):
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

@login_required
def contact(request):
	title = "Contactez-nous maintenant!"
	form  = ContactModelForm(request.POST or None)
	context= {
            "title": title,
            "form": form
    }
	if form.is_valid():
		instance = form.save(commit = False)
		name = form.cleaned_data.get("Last_name")
		if not name:
			name = "Nouveau nom de Famille"
			instance.name = name
			instance.save()
			context = {
				"title": "Merci"
			}
		if request.user.is_authenticated and request.user.is_staff:
			queryset = ContactModel.objects.all().order_by('-timestamp')
			context = {
				"queryset": queryset
			}

	return render(request, "website/contact.html", context)

def registration_bridge(request):
	return render(request, 'website/login_as.html')
