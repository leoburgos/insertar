from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.conf.urls.defaults import *
from piston.resource import Resource
from appInsercion.handlers import InsertHandler

insert_handler = Resource(InsertHandler)

urlpatterns = patterns('appInsercion.handlers',
    # Examples:
    # url(r'^$', 'Insercion.views.home', name='home'),
    # url(r'^Insercion/', include('Insercion.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^insertar/$', insert_handler, name="insert"),
)
