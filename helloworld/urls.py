from django.conf.urls import patterns, include, url
from app import views

urlpatterns = patterns('',
	url(r'^$', 'app.views.home', name='home'),
	url(r'^search', 'app.views.search', name='search'),
)
