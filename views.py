from django.template.loader import get_template
from django.http import HttpResponse, Http404
from django.template import Context
from django.shortcuts import render
import calc


import datetime



def text_to(request):
    return render(request, 'text.html')
#def get_text(request):
#    t = request.GET['q']
 #   y = calc.calc(t)
#    return HttpResponse(y)

def get_text(request):
    t = request.GET['q']
    y = calc.calc(t)
    return render(request, 'hex.html', {'result': y})

def home(request):
    return HttpResponse("Это домашняя страница")
 
def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'templates.html', {'current_date': now})
        
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'templates3.html', {'time_will': offset, 'will_be': dt})
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    #return HttpResponse(html)
