"""Copyright Askbot SpA 2014, Licensed under GPLv3 license."""
from unicodedata import name
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import re_path, path
from directory import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    re_path(r'^(?P<path>.*)$', views.browse, name='directory_browse'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
