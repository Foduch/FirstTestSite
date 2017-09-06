from django.conf.urls import url
from django.contrib import admin
from testapp.views import somefunc, athletes_list

urlpatterns = [
    url(r'^some/', somefunc, name = 'somefunc'),
    url(r'^athletes/', athletes_list, name = 'athletes_list'),
]
