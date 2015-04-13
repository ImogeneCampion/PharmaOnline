from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpRequest
from django.http import HttpResponse

def homie(request):
		assert isinstance(request, HttpRequest)
		return render(
			request,
			'helloworld/templates/app/index.html',
			context_instance = RequestContext(request,
			{
				'title': 'accueil',
			})
		)

def home(request):
	return render(request, 'app/basis.html')