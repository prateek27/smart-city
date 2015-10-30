from django.conf.urls import patterns, include, url
from django.contrib import admin
from material.frontend import urls as frontend_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smartcity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include(frontend_urls)),
    url(r'^',include('login.urls')),
   	url(r'^representative/',include('representative.urls')),
    url(r'^citizen/',include('citizen.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
