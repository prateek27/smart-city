from django.conf.urls import patterns, include, url
from django.contrib import admin
from material.frontend import urls as frontend_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smartcity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include(frontend_urls)),
    url(r'^',include('login.urls')),

)
