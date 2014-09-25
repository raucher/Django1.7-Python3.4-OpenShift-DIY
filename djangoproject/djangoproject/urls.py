from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.http import HttpResponse
def index(request):
    return HttpResponse("<p><b>Congratulations! You Django 1.7 with Python 3.4 running on OpenShift!</b></p><p>You can access the admin <a href='/admin'>here</a> but don't forget you must first create a superuser.</p>")

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
)
