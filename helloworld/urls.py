from django.conf.urls import patterns, include, url
from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helloworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^/', include(app.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
