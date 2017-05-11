from django.conf.urls import url, include
from django.contrib import admin
from contact import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact/', include('contact.urls')),
    url(r'^rest/contacts', views.ContactList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)