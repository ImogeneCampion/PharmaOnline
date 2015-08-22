from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Pharmacie

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
