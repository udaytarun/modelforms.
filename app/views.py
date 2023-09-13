from django.shortcuts import render
from app.forms import*
from app.models import*
from django.http import HttpResponse


# Create your views here.
def insert_topic(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}


    if request.method=='POST':

        DTFO=Topicform(request.POST)
        if DTFO.is_valid():
            DTFO.save()
            return HttpResponse('TOPIC IS CREATED.....')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    UTFO=Webpageform()
    d={'UTFO':UTFO}


    if request.method=='POST':

        UTWO=Webpageform(request.POST)
        if UTWO.is_valid():
            UTWO.save()
            return HttpResponse('webpage is created..')
    return render(request,'insert_webpage.html',d)