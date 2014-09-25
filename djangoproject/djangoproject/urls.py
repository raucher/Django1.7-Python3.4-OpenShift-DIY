from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.http import HttpResponse
def index(request):
    return HttpResponse("Congratulations!. You are running Python 3 and Django 1.7 on OpenShift!")

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
)
