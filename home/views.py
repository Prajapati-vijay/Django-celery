from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import time
from .task import task_manage
from django.shortcuts import render
from celery.result import AsyncResult

def Home(request):
    # time.sleep(10)
    r=task_manage.delay(20,30)
    print("Result",r)
 
    return render(request,'index.html',{'status':r.status,'id':r})    



def Task(request,id):
    result=AsyncResult(id)
    return render(request,'Home.html',{'result':result,'id':id})