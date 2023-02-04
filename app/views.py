from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import *

# Create your views here.
def Insert_Topic_model(request):
    form = TopicForm()
    d={'form':form}
    if request.method=='POST':
        FD = TopicForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('Topic data inserted using Model Form')
    return render(request,'Insert_Topic_model.html',d)
def Insert_webpage_model(request):
    form = WebpageForm()
    d={'form':form}
    if request.method=='POST':
        FD = WebpageForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('Webpage data inserted using Model Form')
    return render(request,'insert_webpage_model.html',d)

def Insert_Access_model(request):
    form = AccessRecordForm()
    d={'form':form}
    if request.method=='POST':
        FD = AccessRecordForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('AccessRecord data inserted using Model Form')
    return render(request,'insert_Access_model.html',d)