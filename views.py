from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from testapp.models import Athlete
import datetime

def somefunc(request):
    context = 'Some text...'
    #return HttpResponse('Hello World!', content_type='text/plain')
    return render(request, 'some', {'text': context,})

def athletes_list(request):
    res = Athlete.objects.all()
    if len(res) > 0:
        return render(request, 'athletes', {'athletes_list': res,})
        #return HttpResponse(str(res[0]),  content_type='text/plain')
    else:
        return render(request, 'athletes', {'athletes_list': res,})
        #return HttpResponse('None', content_type='text/plain')

def add_athlete(request):
    try:
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        sex = request.GET.get('sex')
        birthday = request.GET.get('birthday')
        birthday = datetime.datetime.strptime(birthday, '%d%m%Y')
        birthday = birthday.date()
    except :
        return HttpResponse('Error', content_type='text/plain')
       
    a = Athlete(first_name=first_name, last_name=last_name, sex=sex, birthday=birthday)
    a.save()
    return HttpResponse('maybe work', content_type='text/plain')




    
# Create your views here.
