#from django.template.loader import get_template
#from django.template import  Context
from django.http import Http404, HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html',{'current_date': now})

#def current_datetime(request):
#    now = datetime.datetime.now()
#    t = Template("<html><body>It is now {{ current_date }}. </body></html>")
#    t = get_template('current_datetime.html')
#    html = t.render({'current_date': now})
#    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request , 'hours_ahead.html', {'hour_offset': offset , 'next_time' : dt} )
#    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % ( offset, dt)
#    return HttpResponse(html)
