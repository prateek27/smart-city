from django.conf.urls import patterns, include, url
from django.contrib import admin
from login.views import *
from representative.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GamingPortal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',representative_view,name="representative_view"),
)
