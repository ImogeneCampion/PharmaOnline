from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import Http404
from app.models import Rx

def home(request):
	return render(request, 'app/squelette.html')
	
def search(request):
	return render(request, 'app/basis.html')