from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Athlete

def somefunc(request):
    return HttpResponse('Hello World!', content_type='text/plain')

def athletes_list(request):
    res = Athlete.objects.all()
    if len(res) > 0:
        return HttpResponse(unicode(res[0]),  content_type='text/plain')
    else:
        return HttpResponse('None', content_type='text/plain')

    
# Create your views here.
