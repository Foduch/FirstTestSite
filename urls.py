from django.conf.urls import url
from django.contrib import admin
import testapp.views
from testapp.views import somefunc, athletes_list, add_athlete

urlpatterns = [
    url(r'^some/', somefunc, name = 'somefunc'),
    url(r'^athletes/', athletes_list, name = 'athletes_list'),
    url(r'^add_athlete', add_athlete, name = 'add_athlete'),
]
