from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
from app.forms import *

def insert_Topic(request):
       TFO=TopicForm()
       d={'TFO':TFO}
       if request.method=='POST':
           TFOD=TopicForm(request.POST)
           
           if TFOD.is_valid():
             TFOD.save()
             return HttpResponse('Topic form data inserted successfully...!')
        

       return render(request,'insert_Topic.html',d)

def insert_Webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}

    if request.method=='POST':
        WFOD=WebpageForm(request.POST)
        if WFOD.is_valid():
            WFOD.save()
            return HttpResponse('Webpage data inserted successfully...!')
    return render(request,'insert_Webpage.html',d)
def insert_AccessRecord(request):
    AFO=AccessForm()
    d={'AFO':AFO}

    if request.method=='POST':
        AFOD=AccessForm(request.POST)
        if AFOD.is_valid():
            AFOD.save()
            return HttpResponse('AccessRecord data inserted successfully...!')
    return render(request,'insert_AccessRecord.html',d)