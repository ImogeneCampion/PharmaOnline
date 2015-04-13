from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpRequest
from django.http import HttpResponse

def home(request):
		assert isinstance(request, HttpRequest)
		return render(
			request,
			'app/index.html',
			context_instance = RequestContext(request,
			{
				'title': 'accueil',
			})
		)
