from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
#view simple hello

def hello_world(request):
    now = datetime.now()

    time =int( now.strftime('%H'))
    msg = 'Hello user good'

    if time < 12 :
        msg = msg+' morning'
    elif time <16 :
        msg = msg+' evening'
    elif time <21 :
        msg = msg+' afternoon'
    else:
        pass
    date_dict = {'date':now, 'age':38, 'name':'Santhosh', 'message':msg}
    return render (request, 'thirdapp/santhus.html', context=date_dict)


def time_given(arg):
    time = datetime.now()
    return HttpResponse('<h1>time to daty is '+str(time)+'</h1>')
