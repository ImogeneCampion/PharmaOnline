from django.conf.urls import patterns, include, url
from django.contrib import admin
from website import views

urlpatterns = patterns('',
    url(r'^$', include('haystack.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^search/', include('haystack.urls')),
	url(r'^pharmacies$', 'website.views.pharmacies', name='pharmacies'),
	(r'^accounts/', include('registration.backends.simple.urls')),
    #url(r'^contact/$', 'website.views.contact', name='contact'),
)
