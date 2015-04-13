from django.conf.urls import patterns, include, url
from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helloworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', app.views.home, name='home'),
)
