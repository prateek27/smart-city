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

    url(r'^$',representative_profile,name="profile_view"),
    url(r'^complaints/',representative_complaints,name="complaints_view"),
    url(r'^projects/',representative_projects,name="projects_view"),
    url(r'^messages/',representative_messages,name="messages_view"),
    url(r'^performance/',representative_quality_checks,name="quality_view"),
    url(r'^calender/',representative_calender,name="calender_view"),
    url(r'^email/',send_message,name="email_view"),
    url(r'^contacts/',representative_contacts_view,name="contacts_view"),
)

