from django.conf.urls import patterns, include, url
from django.contrib import admin
from login.views import *
from representative.views import *
from django.conf.urls.static import static
from django.conf import settings
from citizen.views import *


urlpatterns = patterns('',
    url(r'^$',citizen_view,name="citizen_view"),
)
